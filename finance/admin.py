from django.contrib import admin
from finance.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
   list_display = ('id', 'user', 'balance') 

@admin.register(TransType)
class TransTypeAdmin(admin.ModelAdmin):
   list_display = ('id', 'name') 

class ProxyResource(resources.ModelResource):
    class Meta:
        model = Transaction


# Register your models here.
@admin.register(Transaction)
# class RecordAdmin(admin.ModelAdmin):
# class RecordAdmin(ImportExportModelAdmin):
class TransectionAdmin(ImportExportActionModelAdmin):
    resource_class = ProxyResource

    list_display = ('id', 'trans_type', 'from_user', 'to_user', 'type', 'amount', 'balance', 'create_date')
    readonly_fields = ["balance"]
    list_per_page = 10
    #def has_add_permission(self, request):
    #  return False
    
    def trans_type(self,obj):
        return obj.trans_type.name

