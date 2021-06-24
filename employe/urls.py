from django.urls import path
from . import views 

app_name = "employe"

urlpatterns = [
   path('employe-info/', views.employe_info, name="employe_info"),
]
