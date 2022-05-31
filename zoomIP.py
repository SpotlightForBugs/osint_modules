#!/bin/python3
# import pyfiglet module

import requests
import json
import sys

print('\033[32m') 

def locate():
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,country,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy")
    resp = data.json()
    print("\nIP address successfully zoomed !\n")
    print("Status: " + resp["status"])
    if resp["status"] == "erreur d'adresse ip": #french lookup tool
        print("E-Message: " + resp["message"])
        sys.exit()
    continent = resp["continent"]
    country = resp["country"]
    region = resp["region"]
    regionname = resp["regionName"]
    city = resp["city"]
    district = resp["district"]
    zip = resp["zip"]
    lat = str(resp["lat"])
    lon= str(resp["lon"])
    timezone = resp["timezone"]
    currency = resp["currency"]
    isp = resp["isp"]
    org = resp["org"]
    asp = resp["as"]
    aspname = resp["asname"]
    reverse_lookup =  resp["reverse"]
    mobile = str(resp["mobile"])
    proxy_used = str(resp["proxy"])


ip = input("\nIP/Url = ")
locate()
print(continent,country)
print('\033[33m')


