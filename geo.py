#!/bin/python3
# import pyfiglet module
import argparse
import requests
import json
import sys

print('') 

def locate():
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,country,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy")
    resp = data.json()
    
    print("Status: " + resp["status"])
    if resp["status"] == "fail": 
        print("Error: " + resp["message"])
        sys.exit()
    continent = resp["continent"]
    country = resp["country"]
    region = resp["region"]
    regionname = resp["regionName"]
    city = resp["city"]
    district = resp["district"]
    zip = resp["zip"]
    lat = str(resp["lat"])
    lon = str(resp["lon"])
    timezone = resp["timezone"]
    currency = resp["currency"]
    isp = resp["isp"]
    org = resp["org"]
    asp = resp["as"]
    aspname = resp["asname"]
    reverse_lookup =  resp["reverse"]
    mobile = str(resp["mobile"])
    proxy_used = str(resp["proxy"])
    if args.gmap:
    	print("\nIP/Url = "+ ip)
    	print("http://www.google.com/maps/place/"+ lat +','+ lon)
    elif args.json:
        print(resp)
    else:
        print("Continent : "+ continent)
        print("Country : "+ country)
        print("Region: " + region)
        print("Region Name : " + regionname)
        print("City : " + city)
        print("District : " + district)
        print("Zip : " + zip)
        print("Latitude : " +lat)
        print("Longitude : " + lon)
        print("http://www.google.com/maps/place/"+ lat +','+ lon)
        print("Timezone : " + timezone)
        print("Currency : " + currency)
        print("ISP : " + isp)
        print("ORG : " + org)
        print("AS : " + asp)
        print("AS Name : " + aspname)
        print("Reverse : " + reverse_lookup)
        print("Mobile : " +mobile)
        print("Proxy : " + proxy_used)
    
        
   
        
  
parser = argparse.ArgumentParser()
g = parser.add_mutually_exclusive_group()

parser.add_argument(
     '-ip','-url',dest='target',action='store',help='specify the target to use CLI'
 )
g.add_argument(
    '-txt',dest='txt',
    action='store_true',
    help='output as text',
    
)
g.add_argument(
    '-json', dest='json',
    action='store_true',
    help='output as json',
)

g.add_argument(
	'-maps','-m',dest='gmap',action='store_true',help='only show the Google maps url'
	)

args = parser.parse_args()

if not args.target:
    ip = input("\nIP/Url = ")
if args.target:
    ip = args.target
locate()
