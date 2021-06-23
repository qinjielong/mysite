from django import forms
import datetime


def get_start_date():
    return datetime.date.today() + datetime.timedelta(-30)

class FilterTransForm(forms.Form):
  
  start_date = forms.DateField(initial=get_start_date, widget=forms.TextInput(attrs={'class':'datepicker'}))
  end_date = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={'class':'datepicker'}))
        
