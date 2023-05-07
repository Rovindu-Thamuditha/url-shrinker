import os
import json
import urllib
import requests


#Setting up API keys

with open('config.json','r') as file:
    data = json.load(file)

CUTTLY_API = data['cuttly-api']
ADFOCUS_API = data['adfocus-api']
SHRINKEARN_API = data['shrinkearn-api']
V2LINKS_API = data['v2links-api']



#Selecting the Service Provider Function

def select_host(host, url):
    if host == 'cuttly':
        short_url = cuttly(url)
    
    elif host == 'adfocus':
        pass

    elif host == 'shrinkearn':
        pass

    elif host == 'v2link':
        pass

    else:
        pass

    return short_url

#Fetching data through the relevant api

def cuttly(url):
    api_endpoint = "http://cutt.ly/api/api.php" 
    url = urllib.parse.quote(url) #Encoding URL
    api_url = f"{api_endpoint}?key={CUTTLY_API}&short={url}"
    cuttly_response = requests.get(api_url).json()
    short_url = cuttly_response["url"]["shortLink"]
    return short_url