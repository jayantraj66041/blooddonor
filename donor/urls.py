from django.urls import path
from donor.views import HomePage, DonorRegister, SearchDonor, SignUp, LogIn, MyEntries, ContactUs

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("logout/", HomePage.as_view(), name="logout"),
    path("donor-register/", DonorRegister.as_view(), name="donor-register"),
    path("donor-register/add/", DonorRegister.as_view(), name="donor-register-add"),
    path("delete-donor/", MyEntries.as_view(), name="delete-donor"),
    path("search-donor/<str:blood_group>/<str:city>/", SearchDonor.as_view(), name="search-donor"),
    path("search-donor/", SearchDonor.as_view(), name="search-donor-post"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", LogIn.as_view(), name="login"),
    path("my-entries/", MyEntries.as_view(), name="my-entries"),
    path("contact-us/", ContactUs.as_view(), name="contact-us"),
]
