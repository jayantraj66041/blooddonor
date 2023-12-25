from django.shortcuts import render, redirect
from django.views import View
from donor.models import Donor
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        
        return super().dispatch(request, *args, **kwargs)

class HomePage(BaseView):
    def get(self, request):
        return render(request, "home.html")
    
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("homepage")

class SignUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, "signup.html")
    
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        url = request.GET.get("url")

        try:

            if password == re_password and not User.objects.filter(username=username).exists():

                user = User()
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = username
                user.set_password(password)
                user.save()

                user = authenticate(username=username, password=password)
                # print("pass2")

                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Account created successfully!!")
            else:
                messages.add_message(request, messages.ERROR, "Validation failed!!")

        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, "Something was wrong!!")

        if url:
            return redirect(url)
        else:
            return redirect("homepage")
    

class LogIn(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Login successfully!!")
        else:
            messages.add_message(request, messages.ERROR, "Wrong credintials!!")

        return redirect("homepage")


class DonorRegister(BaseView):
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
                messages.add_message(request, messages.WARNING, "You have already registered!!")

            elif name and blood_group and contact and city:
                d = Donor()
                d.name = name
                d.blood_group = blood_group
                d.email = email
                d.contact = contact
                d.city = city
                d.user = request.user
                d.save()
                messages.add_message(request, messages.SUCCESS, "Thanks for registering as a voluntary blood donor.❤️")

            else:
                messages.add_message(request, messages.INFO, "Invalid Data!!")

        except:
            messages.add_message(request, messages.ERROR, "Something was wrong!!")

        return redirect("donor-register")
    

class SearchDonor(BaseView):
    def get(self, request, *args, **kwargs):
        blood_group = kwargs.get("blood_group")
        city = kwargs.get("city")

        donors = Donor.objects.filter(blood_group=blood_group, city=city.lower()).exclude(status="Inactive")

        return render(request, "search-donor.html", {
            'donors': donors
        })

    def post(self, request):
        blood_group = request.POST.get("blood-group")
        city = request.POST.get('city')

        if blood_group and city:
            return redirect("search-donor", blood_group, city)
        
        return redirect("homepage")


class MyEntries(BaseView):
    def get(self, request, *args, **kwargs):
        return render(request, "my-entries.html", {
            'donors': Donor.objects.filter(user=request.user, status="Active")
        })
    
    def post(self, request, *args, **kwargs):
        donor_id = request.POST.get("donor-id")
        donor = Donor.objects.get(id=donor_id)
        donor.status = "Inactive"
        donor.save()

        return redirect("my-entries")
    

class ContactUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact-us.html")
    
    def post(self, request, *args, **kwargs):
        pass