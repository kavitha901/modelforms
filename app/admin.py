from django.contrib import admin

# Register your models here.
from app.models import *

class CustomizeWebpage(admin.ModelAdmin):
    list_display=['name','topic_name','email','url']
    list_display_links=['url']
    list_editable=['name','topic_name']
    list_per_page=3
    list_filter=['name','url']
    search_fields=['email']

admin.site.register(Topic)
admin.site.register(Webpage,CustomizeWebpage)
admin.site.register(AccessRecord)


