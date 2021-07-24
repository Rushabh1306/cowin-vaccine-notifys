# Setup to run script.
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cowin_vaccine.settings')
django.setup()

#Required Libraries
import email
import smtplib
import requests
from datetime import datetime

#Environment setup
from decouple import config

# In-project resources
from cowin.models import UserFilter

#Time
import time

# Base URLS
district_base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?"
pincode_base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
today_date = datetime.now().strftime("%d-%m-%Y")
state_base_url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
all_users = UserFilter.objects.all()

def collectResult(users):
    for user in users:
        list_of_centers = forPincode(user.pincode)
        print(list_of_centers)
        # sendEmails(list_of_centers,user.email)


# os.environ['mail_sender']="rushabhsoni1306@gmail.com"
# os.environ['mail_password']="btuzevuvayrubtbl"


#Data for pincode
def forPincode(pincode):
    params = {'pincode':pincode,'date':today_date}
    response = requests.get(pincode_base_url,params)
    response = response.json()
    list_of_centers = fetch_required_data(response)
    return list_of_centers
    
# Data for district
def forDistrict(district_id):
    params = {'district_id':district_id,'date':today_date}
    response = requests.get(district_base_url,params)
    response = response.json()
    list_of_centers = fetch_required_data(response)
    return list_of_centers


# Fetching the data and converted to dictionary(context)
def fetch_required_data(response):
    list_of_centers = []
    for center in response['centers']:
        for session in center['sessions']:
            context = {}
            context['date']=session['date']
            context['centre_name'] = center["name"]
            context['address'] = center["address"]
            context['fee_type'] = center["fee_type"]
            context['vaccine'] = session["vaccine"]
            context['age'] = session["min_age_limit"]
            context['dose1'] = session["available_capacity_dose1"]
            context['dose2'] = session["available_capacity_dose2"]
            context['slots'] = session['slots']
            list_of_centers.append(context)
    return list_of_centers

# Creating message for mail
def create_output_message(session):
    return "Center Name : {center_name}\n Center Address : {addr}\n Age : {age}\n Type : {ft}\n Vaccine : {vac}\n Available Dose1 : {dose1}\n Available Dose2 : {dose2}\n Slots : {slots}".format(
        center_name = session['centre_name'],addr = session['address'], 
        ft = session['fee_type'], vac = session['vaccine'],
        dose1 = session['dose1'], dose2 = session['dose2'],
        slots = session['slots'],age = session['age'])


def sendEmails(list_of_centers,receiver):
    # Receiver's Mail
    mail_receiver = receiver
    
    #Sender Mail Authentication
    mail_sender = config('MAIL_SENDER')
    mail_password = config('MAIL_PASSWORD')

    #content of mail
    mail_subject = "Vaccine Slot Alert"
    content_header = "Vaccine Guide Slot Availability Status\nHello {receiver}"
    content = "\n----------------------------------------------------------------\n".join([create_output_message(session) for session in list_of_centers])
    content_footer = "\nThanks!\n Vaccine Guide Team"

    #Sending mails 

    if not content:
        print('No availability')
    else:
        print("Email-Delivering")
        email_msg = email.message.EmailMessage()
        email_msg['subject'] = mail_subject
        email_msg['from'] = "Vaccine Guide"
        email_msg['to'] = mail_receiver
        email_msg.set_content(content_header+content+content_footer)
        print("Email Content Done...")

        with smtplib.SMTP(host='smtp.gmail.com',port='587') as server:
            server.starttls()
            server.login(mail_sender,mail_password)
            print("Email Login Done")
            server.send_message(email_msg,mail_sender,mail_receiver)
            print('Mail Delivered')
            return
    print('Not Delivered!')

# Loops for mails
print()
collectResult(all_users)