from .models import UserFilter
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserFilterForm(ModelForm):
	class Meta: 
		model = UserFilter
		fields = ('email','age','vaccine_type','vaccine_name','pincode')