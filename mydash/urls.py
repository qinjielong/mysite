from django.urls import path 
from . import views 

app_name = 'mydash'

urlpatterns = [
    #path('index/', views.sales_tracker, name='index'), 
    path('index/', views.index, name='index'), 
    path('demo-eight/',views.session_state_view, name="demo-eight"),   
]

