from django.contrib import admin
from .models import  CommunityEntity
# Register your models here.

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('house_number','primary_owner', 'num_people','longitude','latitude')
   
  #  readonly_fields = ('work_order', 'description','assigned_group','date_opened','date_completed')

    fieldsets = [
        ('Unit Information', {
            'fields': ('house_number','primary_owner', 'num_people','longitude','latitude'),
        }),
    ]

admin.site.register(CommunityEntity, CommunityAdmin)