from django.shortcuts import render
from django.http import HttpResponse
from account.models import UserInfo
from .models import Employe


# Create your views here.
def employe_info(request):
  try:
    user = UserInfo.objects.get(user=request.user)
    employe = Employe.objects.get(id=user.employe_id)
    return render(request, "employe/employe_info.html", {'employe':employe})
  except:
    return HttpResponse('对不起，你还不是员工，请联系管理员。')
    
