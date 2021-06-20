from account.models import UserInfo

#试图将数据传递给布局’base.html’.我目前正在通过将数据存储在request.session中并通过请求对象在“base.html”中访问它来实现.
#没有办法将数据传递给’base.html’而无需从每个视图传递数据


def add_userinfo_to_context(request):
    if request.user.is_authenticated:
      try:
        userinfo = UserInfo.objects.get(user=request.user) 
        if hasattr(request.user, 'userinfo'): 
          return {"user":request.user, "userinfo":userinfo}
        
      except:
        return {"user":request.user}
    else:
      return {"user":request.user}
