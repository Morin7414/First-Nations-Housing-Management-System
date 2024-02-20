from django.contrib import admin
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountInline(admin.StackedInline):
    model = Account
    can_delete =False
    verbose_name_plural = 'Accounts'

class AccountAdmin(UserAdmin):
    inlines  = [AccountInline]
    list_display = ('username',  'email', 'first_name', 'last_name','get_phone', 'get_cell',)


    def get_phone(self, obj):
        return obj.account.work_phone if hasattr(obj, 'account') else None
    

    def get_cell(self, obj):
        return obj.account.cell_phone if hasattr(obj, 'account') else None


    get_phone.short_description = 'Work Phone'
    get_cell.short_description = 'Cell Phone'

admin.site.unregister(User)
admin.site.register(User, AccountAdmin)
