import logging
from django.contrib import admin
from .models import  WorkOrder, Task
import boto3
from botocore.exceptions import ClientError
from django.utils.html import mark_safe
from django.conf import settings
from order.models import Quote
from django.template.loader import get_template


############################################################################################################
 # Inlines
class TaskInline(admin.TabularInline):
    model = Task
    fields = ('status', 'description','assigned_group', 'image_preview')
    readonly_fields = ('description','image_preview')
    extra = 0
 #  template = 'admin/inline_model.html'


    def has_delete_permission(self, request, obj=None):
        return False  # Disable deleting existing records
    
 #   def has_add_permission(self, request, obj=None):
        # Allow adding new rows only if the parent object has been saved
    #    return obj is not None and obj.pk
    def has_add_permission(self, request, obj=None):
        # Disable the "Add another" button
         return False
    
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        # Exclude the 'diagnostics' field
        fields = [field for field in fields if field not in  ['date_opened','image', 'assigned_worker']]
        return fields
    
    def image_preview(self, obj):
        try:
            if obj.image:
                logging.debug("Image_key!!!: %s", obj.image)
                image_key = obj.image
                s3_client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name='ca-central-1', config=boto3.session.Config(signature_version='s3v4')) 
                url = s3_client.generate_presigned_url('get_object',
                                                  Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': f'{obj.image}'},
                                                  ExpiresIn=900) 
                return mark_safe(f'<a href="{url}"><img src="{url}" style="max-width: 100px; max-height: 100px;" /></a>')
            else:
                return ""  # Return an empty string or any default value when there is no image
        except ClientError as e:
            return f"Error generating URL: {e}"
        
  


class QuoteInline(admin.TabularInline):
    model = Quote
    list_display = ('worker','amount',)

################################################################################################################
    #ADMIN 

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('status','house','coordinator', 'date_opened', 'date_closed', )
    inlines = [TaskInline]
   
   
    fieldsets = [
       
        ('Work Order Information', {
            'fields': ('status','house','coordinator', 'date_opened', 'date_closed','subject'),
        }),
     
         ('Add Task', {
            'fields': ('image', 'assigned_group', 'description',),
        }),
    ]

 
  

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        Task.objects.create(ticket=obj, status=obj.status, description=obj.description, image = obj.image, assigned_group = obj.assigned_group)
        obj.description = "" 
        obj.image = ""
    
        obj.save()


class TaskAdmin(admin.ModelAdmin):
    list_display = ('status', 'description','assigned_worker',)
    inlines = [QuoteInline]



admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(Task, TaskAdmin)



