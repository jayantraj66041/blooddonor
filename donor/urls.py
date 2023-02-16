from django.urls import path
from donor.views import HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
]
