from .forms import UserFilterForm
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .utils import forDistrict, forPincode
from .models import StatesList, DistrictList

# Create your views here.
def indexView(request):
    states = StatesList.objects.all()
    districts = DistrictList.objects.all()
    context={}
    context['states'] = states
    context['districts'] = districts
    data = None
    if request.method=='POST':
        print(request.POST)
        if request.POST['pin']:
            data = forPincode(int(request.POST['pin']))
        if request.POST['dist']:
            data = forDistrict(request.POST['dist'])
    context['data']=data
    print(data)
    return render(request,'index.html',context)

def notificationView(request):
    context = {}
    user_form = UserFilterForm()
    print(request.POST)
    if request.method=='POST':
        user_form = UserFilterForm(request.POST)
        print(user_form)
        email = user_form.cleaned_data['email']
        if user_form.is_valid():
            user_form.save()
    context['user_form']=user_form
    return render(request,'notifications.html',context)