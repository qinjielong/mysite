from django.shortcuts import render
from account.models import UserInfo

def home(request):
      if request.user.is_authenticated:
        try:
          userinfo = UserInfo.objects.get(user=request.user) 
          if hasattr(request.user, 'userinfo'): 
            return render(request, "home/home.html", {"user":request.user, "userinfo":userinfo})
        
        except:
          return render(request, "home/home.html", {"user":request.user})
      else:
        return render(request, "home/home.html", {"user":request.user})


def about(request):
      if request.user.is_authenticated:
        try:
          userinfo = UserInfo.objects.get(user=request.user)
          if hasattr(request.user, 'userinfo'): 
            return render(request, "home/about.html", {"user":request.user, "userinfo":userinfo})
        except:
          return render(request, "home/about.html", {"user":request.user})
      else:
        return render(request, "home/about.html", {"user":request.user})

        

# Create your views here.
