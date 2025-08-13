from django.shortcuts import render
import requests
from datetime import datetime , timedelta


ACCESS_TOKEN = 'sk_TcbakQt5472PX3Jr'

def home(request):

    long_url = ''
    short_url = ''
    if request.POST:
        long_url = request.POST.get('long_url')
        print(f"the long url is : {long_url}")

        short_url = url_shortener(long_url)

        short_url = 'https://' + short_url

        print(f"the short_url is : {short_url}")


    context = {
        'short_url' : short_url
    }
  
    return render(request , 'home/index.html' , context)


API_KEY = "631851a3a1e64e159a22a42f1df51afe"

def url_shortener(long_url):
    url = "https://api.rebrandly.com/v1/links"
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "destination": long_url,
        "domain": { "fullName": "rebrand.ly" }
    }
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code in (200, 201):
        return r.json()["shortUrl"]
    else:
        return r.text
