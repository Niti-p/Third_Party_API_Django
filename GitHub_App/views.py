import requests

import json
import urllib.request

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# def ViewUser(request):
#     url = "https://api.github.com/users/"
#     if request.method == 'POST':
#         username = request.POST['users']
#         fetch_url = url+username
#         response = requests.get(fetch_url)
#         username = " "
#         print(response)
#         if response.status_code == 200:
#             response_data = response.json()
#             return render(request, 'GitHub_App/homepage.html', {"data":response_data})
#         else:
#             error_data = {
#                 "error_msg": "Sorry! Not Found , Please Try Again with Right GitHub Username"
#             }
#             return render(request, 'GitHub_App/errorpage.html', error_data)
        
#     return render(request, 'GitHub_App/homepage.html')

def ViewUser(request):
    url = "https://api.github.com/users/"
    if request.method == 'POST':
        username = request.POST['users']
        response = urllib.request.urlopen(url+username)
        text = response.read()
        print(json.loads(text.decode('utf-8')))
        if response.status_code == 200:
            response_data = response.json()
            return render(request, 'GitHub_App/homepage.html', {"data":response_data})
        else:
            error_data = {
                "error_msg": "Sorry! Not Found , Please Try Again with Right GitHub Username"
            }
            return render(request, 'GitHub_App/errorpage.html', error_data)
        
    return render(request, 'GitHub_App/homepage.html')


