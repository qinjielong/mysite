from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, FormView
from django.db.models import Sum
import datetime

from .models import Account, Transaction, TransType
from .forms import FilterTransForm
from braces.views import LoginRequiredMixin
from django.contrib.auth.models import User

def check_add_account(user):
  account = {}
  try:
    account = Account.objects.get(user=user)
  except:
    account = Account()
    account.user = user
    account.balance = 0
    account.save()
  return account

def get_admin():
  try:
    user = User.objects.get(username='admin') 
    return user
  except:
    return

def user_coin_trans(user, from_user, to_user, trans_type, amount, type):
          trans = Transaction()
          trans.trans_type = trans_type
          trans.user = user
          trans.from_user = from_user
          trans.to_user = to_user 
          trans.amount = amount
          trans.create_date = datetime.datetime.now()
          trans.type = type
         
          account = check_add_account(user) 
          return account.update_balance(trans)

def coin_trans(from_user, to_user, trans_type, amount):
    ok = user_coin_trans(from_user, from_user, to_user, trans_type, -amount, 1)
    if ok:
      ok = user_coin_trans(to_user, from_user, to_user, trans_type, amount, 0)
    
    return ok


def publish_article_coin_trans(admin, author):
     ok = False 
     try:
          trans_type = TransType.objects.get(name='发表文章')
	  
	  # 从系统,即管理员扣10个银币
          # 作者获得10个银币
          ok = coin_trans(admin, author, trans_type, 10)
     except:
          return False
     return ok

def comment_article_coin_trans(user, author):
     ok = False 
     try:
          trans_type = TransType.objects.get(name='发表评论')
	  
	  # 扣用户2个银币
          # 作者获得2个银币
          ok = coin_trans(user, author, trans_type, 2)
     except:
          return False
     return ok

def edit_userinfo_coin_trans(user, admin):
     ok = False 
     try:
          trans_type = TransType.objects.get(name='个人信息修改')
	  
	  # 扣用户5个银币
          # 系统获得5个银币
          ok = coin_trans(user, admin, trans_type, 5)
     except:
          return False
     return ok


class AccountView(View): 

    def get_context_data(self, *args, **kwargs):
        filter_form = FilterTransForm()
        user = kwargs['user']
        account = check_add_account(user)
        start_date = kwargs['start_date']
        end_date = kwargs['end_date']
        transactions = Transaction.objects.filter(user=user, create_date__range=[start_date, end_date]).order_by('create_date', 'id')
        context = {'transactions': transactions, 'account': account, 'filter_form': filter_form}
        return context


    def get(self, request):
        thirty_days_ago = datetime.datetime.today() + datetime.timedelta(-30)
        start_date = thirty_days_ago.strftime('%Y-%m-%d %H:%M:%S')
        end_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'finance/overview.html', self.get_context_data(request, user=request.user, start_date=start_date, end_date=end_date))


    def post(self, request):
        start_date =0
        end_date = 0
        
        filter_form = FilterTransForm(request.POST, prefix='filter_form')
        if filter_form.is_valid():
            start_date = filter_form.cleaned_data['start_date'].strftime('%Y-%m-%d %H:%M:%S')
            end_date = filter_form.cleaned_data['end_date'].strftime('%Y-%m-%d %H:%M:%S')
        else:
            thirty_days_ago = datetime.datetime.today() + datetime.timedelta(-30)
            start_date = thirty_days_ago.strftime('%Y-%m-%d %H:%M:%S')
            end_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        return render(request, 'finance/overview.html',  self.get_context_data(request, user=request.user, start_date=start_date, end_date=end_date))

def about_coin(request):
  return render(request, "finance/about_coin.html")

