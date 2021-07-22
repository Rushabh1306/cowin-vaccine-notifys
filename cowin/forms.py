from .models import Filter, UserFilter
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class FilterForm(ModelForm):
	class Meta: 
		model = Filter
		fields = ('age','vaccine_type','vaccine_name','pincode')

class UserFilterForm(ModelForm):
	class Meta: 
		model = UserFilter
		fields = ('email','age','vaccine_type','vaccine_name','pincode')