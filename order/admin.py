import logging
from django.contrib import admin
from .models import  Quote
import boto3
from botocore.exceptions import ClientError
from django.utils.html import mark_safe
from django.conf import settings



class QuoteAdmin(admin.ModelAdmin):
    list_display = ('status','task','amountCAD','date_requested')
    list_filter = ('status',)
    readonly_fields = ('task', 'date_requested','image_preview')

    fieldsets = [
        ('Quote Information', {
            'fields': ('task','status','date_requested','amountCAD', 'image_preview', ),
        }),
        
    ]

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
        
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_delete'] = False
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


# Register your models here.
admin.site.register(Quote,QuoteAdmin)