from django.contrib import admin
from finance.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Transaction


# Register your models here.
@admin.register(Transaction)
# class RecordAdmin(admin.ModelAdmin):
# class RecordAdmin(ImportExportModelAdmin):
class TransectionAdmin(ImportExportActionModelAdmin):
    resource_class = ProxyResource

    list_display = ('id', 'name', 'from_user', 'to_user', 'type', 'amount', 'balance', 'create_date')
    readonly_fields = ["balance"]
    list_per_page = 10
    def has_add_permission(self, request):
      return False

