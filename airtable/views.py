from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import requests

@login_required
def airtable(request):
    api_key = "keyC4bESDAqJVg3gb"
    api_url = "https://api.airtable.com/v0/appx2CBZANmioaAxs/Tasks?maxRecords=3&view=Grid%20view"
    headers = {
        "Authorization": "Bearer " + api_key
    }
    json = {
        "maxRecords": "100"
    }
    h = requests.get(api_url, headers=headers, params=json)
    return render(request, 'airtable/airtable.html', {'result': h.json()['records']})

@login_required
def delete(request, pk):
    api_key = "keyC4bESDAqJVg3gb"
    api_url = "https://api.airtable.com/v0/appx2CBZANmioaAxs/Tasks"
    headers = {
        "Authorization": "Bearer " + api_key
    }
    params = f'records[]={pk}'
    requests.delete(api_url, headers=headers, params=params)
    return redirect('airtable')

@login_required
def create(request):
    if request.method == "POST":
        api_key = "keyC4bESDAqJVg3gb"
        api_url = "https://api.airtable.com/v0/appx2CBZANmioaAxs/Tasks"
        headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
        }
        Name = request.POST["Name"]
        Status = request.POST["Status"]
        Priority = request.POST["Priority"]
        StartDate = request.POST["StartDate"]
        Deadline = request.POST["Deadline"]
        params = {
            "records": [{
                "fields": {
                    "Name": Name,
                    "Status": Status,
                    "Priority": Priority,
                    "Start date": StartDate,
                    "Deadline": Deadline
                }
            }]
        }
        requests.post(api_url, headers=headers, json=params)
    return render(request, 'airtable/create.html')

@login_required
def edit(request, pk):
    api_key = "keyC4bESDAqJVg3gb"
    api_url = "https://api.airtable.com/v0/appx2CBZANmioaAxs/Tasks?maxRecords=3&view=Grid%20view"
    headers = {
        "Authorization": "Bearer " + api_key
    }
    json = {
        "maxRecords": "100"
    }
    h = requests.get(api_url, headers=headers, params=json)
    a = ''
    b = ''
    for i in range(len(h.json())):
        if h.json()["records"][i]["id"] == pk:
            a = h.json()["records"][i]
            b = h.json()["records"][i]["fields"]["Start date"]
    if request.method == "POST":
        api_key = "keyC4bESDAqJVg3gb"
        api_url = "https://api.airtable.com/v0/appx2CBZANmioaAxs/Tasks"
        headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
        }
        Name = request.POST["Name"]
        Status = request.POST["Status"]
        Priority = request.POST["Priority"]
        StartDate = request.POST["StartDate"]
        Deadline = request.POST["Deadline"]
        params = {
            "records": [{
                "id": f'{pk}',
                "fields": {
                    "Name": Name,
                    "Status": Status,
                    "Priority": Priority,
                    "Start date": StartDate,
                    "Deadline": Deadline
                }
            }]
        }
        h = requests.patch(api_url, headers=headers, json=params)
        return redirect('airtable')
    return render(request, 'airtable/edit.html', {"content": a, 'startDate': b})