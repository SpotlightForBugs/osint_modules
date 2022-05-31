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
    if resp["status"] == "erreur d'adresse ip":
        print("E-Message: " + resp["message"])
        sys.exit()
    print("Continent : " + resp["continent"])
    print("Country : " + resp["country"])
    print("Region: " + resp["region"])
    print("Region Name : " + resp["regionName"])
    print("City : " + resp["city"])
    print("District : " + resp["district"])
    print("Zip : " + resp["zip"])
    print("Latitude : " + str(resp["lat"]))
    print("Longitude : " + str(resp["lon"]))
    print("Timezone : " + resp["timezone"])
    print("Currency : " + resp["currency"])
    print("ISP : " + resp["isp"])
    print("ORG : " + resp["org"])
    print("AS : " + resp["as"])
    print("AS Name : " + resp["asname"])
    print("Reverse : " + resp["reverse"])
    print("Mobile : " + str(resp["mobile"]))
    print("Proxy : " + str(resp["proxy"]))


ip = input("\nIP/Url = ")
locate()

print('\033[33m')

print("Twitter : @Tenkahashi  | Github : Tenkahashi ")

