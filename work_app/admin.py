from django.contrib import admin
from .models import About
from .models import Blog

# Register your models here.
admin.site.register(About)
admin.site.register(Blog)