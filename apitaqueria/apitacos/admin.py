from django.contrib import admin
from .models import TacosModel

class TacosModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(TacosModel, TacosModelAdmin)

# Register your models here.
