from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Pdf Genarator"
admin.site.site_title = "Pdf Genarator"
admin.site.index_title = "Pdf Genarator"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)
    fields = ('name','email')
    list_editable = ('email',)


admin.site.register(Profile,ProfileAdmin)
