from django.urls import path
from .views import AccountView
from . import views 

app_name = "finance"

urlpatterns = [
   path('finance-overview/', AccountView.as_view(), name="finance_overview"),
   path('about-coin/', views.about_coin, name="about_coin"),
]
