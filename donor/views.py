from django.shortcuts import render, redirect
from django.views import View
from donor.models import Donor
from django.contrib import messages
from django.db.models import Q

# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, "home.html")
    

class DonorRegister(View):
    def get(self, request):
        return render(request, "donor-register.html")
    
    def post(self, request):
        name = request.POST.get("name")
        blood_group = request.POST.get("blood-group")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        city = request.POST.get("city").lower()

        try:
        
            if Donor.objects.filter(contact=contact).count():
                print("----------------------")
                messages.add_message(request, messages.WARNING, "You have already registered!!")

            elif name and blood_group and contact and city:
                d = Donor()
                d.name = name
                d.blood_group = blood_group
                d.email = email
                d.contact = contact
                d.city = city
                d.save()
                messages.add_message(request, messages.SUCCESS, "Thanks for registering as a voluntary blood donor.❤️")

            else:
                messages.add_message(request, messages.INFO, "Invalid Data!!")

        except:
            messages.add_message(request, messages.ERROR, "Something was wrong!!")

        return redirect("donor-register")
    

class SearchDonor(View):
    def get(self, request, *args, **kwargs):
        blood_group = kwargs.get("blood_group")
        city = kwargs.get("city")

        donors = Donor.objects.filter(blood_group=blood_group, city=city.lower())

        return render(request, "search-donor.html", {
            'donors': donors
        })

    def post(self, request):
        blood_group = request.POST.get("blood-group")
        city = request.POST.get('city')

        if blood_group and city:
            return redirect("search-donor", blood_group, city)
        
        return redirect("homepage")
