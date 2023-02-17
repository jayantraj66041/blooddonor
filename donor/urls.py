from django.urls import path
from donor.views import HomePage, DonorRegister, SearchDonor

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("donor-register/", DonorRegister.as_view(), name="donor-register"),
    path("donor-register/add/", DonorRegister.as_view(), name="donor-register-add"),

    path("search-donor/<str:blood_group>/<str:city>/", SearchDonor.as_view(), name="search-donor"),
    path("search-donor/", SearchDonor.as_view(), name="search-donor-post"),
]
