from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, FormView
from django.db.models import Sum
import datetime

from .models import Account, Transaction
from .forms import FilterTransForm
from braces.views import LoginRequiredMixin

class AccountView(View): 

    def get_context_data(self, *args, **kwargs):
        filter_form = FilterTransForm()
        user = kwargs['user']
        account = {}
        try:
          account = Account.objects.get(user=user)
        except:
          account = Account()
          account.user = user
          account.balance = 0
          account.save()

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
        account = Account.objects.get(user=request.user)
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





