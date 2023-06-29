import os
import json
import urllib
import requests
import tkinter as tk
from tkinter import messagebox



#Setting up API keys

with open('config.json','r') as file:
    data = json.load(file)

CUTTLY_API = data['cuttly-api']
ADFOCUS_API = data['adfocus-api']
SHRINKEARN_API = data['shrinkearn-api']
V2LINKS_API = data['v2links-api']



#Selecting the Service Provider Function

"""def select_host(host, url):
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

    return short_url"""

#Fetching data through the relevant api

def cuttly(url):
    api_endpoint = "http://cutt.ly/api/api.php" 
    url = urllib.parse.quote(url) #Encoding URL
    api_url = f"{api_endpoint}?key={CUTTLY_API}&short={url}"
    cuttly_response = requests.get(api_url)
    cuttly_response_json = cuttly_response.json()

    if cuttly_response.status_code == 200:
        short_url = cuttly_response_json["url"]["shortLink"]
        status = cuttly_response_json['url']['status']
        return short_url, status
    
    else:
        try:
            status = cuttly_response_json['url']['status']
            return None, status
            """error_msg = messagebox.showerror(f"Error {cuttly_response.status_code}" , "Error occured")
            return error_msg"""

        except:
            status = cuttly_response_json['message']
            error_msg = messagebox.showerror(f"Invalid API Key" , "Please add your api key to the config.json file.")
            return None, error_msg

    
def adfocus():
    error_msg = messagebox.showwarning(f"Coming Soon" , "Still we are working on this feature")
    return error_msg
def shrinkearn():
    error_msg = messagebox.showwarning(f"Coming Soon" , "Still we are working on this feature")
    return error_msg
    
def v2links():
    error_msg = messagebox.showwarning(f"Coming Soon" , "Still we are working on this feature")
    return error_msg

def bitly():
    error_msg = messagebox.showwarning(f"Coming Soon" , "Still we are working on this feature")
    return error_msg

