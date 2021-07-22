from django.contrib import admin
from .models import StatesList,DistrictList, UserFilter
# Register your models here.
admin.site.register(StatesList)
admin.site.register(DistrictList)
admin.site.register(UserFilter)