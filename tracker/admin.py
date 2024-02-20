import logging
from django.contrib import admin
from .models import  WorkOrder, Task, History
import boto3
from botocore.exceptions import ClientError
from django.utils.html import mark_safe
from django.conf import settings
from order.models import Quote
from django.template.loader import get_template
from django.utils import timezone


############################################################################################################
 # Inlines
class TaskInline(admin.TabularInline):
    model = Task
    fields = ('status','assigned_group', 'description','date_opened', 'date_completed')
   # readonly_fields = ('id',)
    extra = 1
    template = "admin/tracker/inline_model.html"
 #  template = 'admin/inline_model.html'
    def has_delete_permission(self, request, obj=None):
        return False  # Disable deleting existing records
 #   def has_add_permission(self, request, obj=None):
        # Allow adding new rows only if the parent object has been saved
    #    return obj is not None and obj.pk
   # def has_add_permission(self, request, obj=None):
        # Disable the "Add another" button
    #     return False
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        # Exclude the 'diagnostics' field
        fields = [field for field in fields if field not in  ['image', 'assigned_worker']]
        return fields
    

    
class HistoryInline(admin.TabularInline):
    model = History
    fields = ('status','assigned_worker', 'diagnostics','date','image_preview',)
    readonly_fields = ('image_preview',)
    ordering = ('-date',) 
    extra = 1
    def has_change_permission(self, request, obj=None):
        return False  # Disable changing existing records
   
    def has_delete_permission(self, request, obj=None):
        return False  # Disable deleting existing records
   
    def has_add_permission(self, request, obj=None):
        # Disable the "Add another" button
         return False
    
    
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
    fields= ('status','amountCAD','image','date_requested')
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False  # Disable changing existing records
   
    def has_delete_permission(self, request, obj=None):
        return False  # Disable deleting existing records

################################################################################################################
    #ADMIN 

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('status','house','coordinator', 'date_opened', 'date_closed', )
    list_filter = ('status',)
    raw_id_fields = ('house',)
    #actions_on_top = False  # Remove actions dropdown from the top
   # actions = None  # Disable the selection checkbox
    inlines = [TaskInline]
    fieldsets = [
        ('Work Order Information', {
            'fields': ('status','house','coordinator', 'date_opened', 'date_closed','subject'),
        }),
        
    ]
  #  def save_model(self, request, obj, form, change):
   #     super().save_model(request, obj, form, change)
    #    Task.objects.create(ticket=obj, status=obj.status, description=obj.description, image = obj.image)
    #    obj.description = "" 
     #   obj.image = ""
    
    #    obj.save()

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_delete'] = False
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('work_order','status', 'assigned_group','description',)
    list_filter = ('assigned_group',)
    inlines = [HistoryInline,QuoteInline]
    readonly_fields = ('work_order', 'description','assigned_group','date_opened','date_completed')

    fieldsets = [
        ('Task Information', {
            'fields': ('work_order','description','assigned_group', 'date_opened', 'date_completed'),
        }),
        ('Diagnostics', {
            'fields': ('status','image','diagnostics',),
        }),
        
    ]


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        History.objects.create(task=obj, status=obj.status, assigned_worker=request.user, image = obj.image, diagnostics = obj.diagnostics, date = timezone.now())
        obj.diagnostics = "" 
        obj.image = ""
    
        obj.save()

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_delete'] = False
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


class HistoryAdmin(admin.ModelAdmin):
     list_display = ('task','status','diagnostics', 'assigned_worker','date',)
     def has_module_permission(self, request):
        # This method determines whether the module (app) is shown in the admin index.
        # Returning False will hide it from the navigation bar.
        return False

admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(History, HistoryAdmin)


