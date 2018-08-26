from django.contrib import admin
from .models import *

class SubsriberAdmin (admin.ModelAdmin):
    #list_display = ['name', 'email']
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ('name',)
    search_fields = ['name', 'email']
    #inlines = [FieldMappingInline]
    #fields = []
    #exclude = ['type']
    #list_filter = ('report_data')
    #search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber,SubsriberAdmin)
# Register your models here.