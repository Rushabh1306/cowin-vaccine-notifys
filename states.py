import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cowin_vaccine.settings')
django.setup()
import requests
from cowin.models import StatesList
state_base_url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
print(StatesList.objects.all())
response = requests.get(state_base_url, headers=headers)
print(response)
response = response.json()
print(response)
# for state in response['states']:
#     print(state['state_id'])
#     print(state['state_name'])

# print("-----------------------------------")

# for i in range(1,37):
#     state_id = i
#     district_base_url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{0}".format(state_id)
#     response = requests.get(district_base_url,headers=headers)
#     response = response.json()
#     for district in response['districts']:
#         print(state_id)
#         print(district['district_id'])
#         print(district['district_name'])
#     print("--------------------------------------------")

