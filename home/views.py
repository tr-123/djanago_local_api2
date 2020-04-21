from django.shortcuts import render
import os
from  django import template
import requests

register = template.Library()

def index(request):
    url = "https://api.exchangeratesapi.io/latest?base=USD"
    response = requests.request("GET", url)
    msg = response.json()
    factor = msg['rates']['INR']
    factor = 77
    return render(request,'index3.html',{'n':factor, })



