from django.contrib import admin

# Register your models here.

from .models import Import, Document

admin.site.register(Import)
admin.site.register(Document)
