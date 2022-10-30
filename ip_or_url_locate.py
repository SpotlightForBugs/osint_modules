#!/bin/python3
# import pyfiglet module
import argparse
import requests
import sys
import os

print()

def clear():
   command = 'clear'
if os.name in ('nt', 'dos'):  #Windows
    command = 'cls'
os.system(command)

def locate():
   data = requests.get(
       f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy"
   )
   resp = data.json()
   print("Status: " + resp["status"])
   if resp["status"] == "fail": 
       print("Error: " + resp["message"])
       sys.exit()
   lat = str(resp["lat"])
   lon = str(resp["lon"])
   if args.gmap:
      print("\nIP/Url = "+ ip)
      print(f"http://www.google.com/maps/place/{lat},{lon}")
   elif args.json:
       print(resp)
   else:
      continent = resp["continent"]
      print(f"Continent : {continent}")
      country = resp["country"]
      print(f"Country : {country}")
      region = resp["region"]
      print(f"Region: {region}")
      regionname = resp["regionName"]
      print(f"Region Name : {regionname}")
      city = resp["city"]
      print(f"City : {city}")
      district = resp["district"]
      print(f"District : {district}")
      zip = resp["zip"]
      print(f"Zip : {zip}")
      print(f"Latitude : {lat}")
      print(f"Longitude : {lon}")
      print(f"http://www.google.com/maps/place/{lat},{lon}")
      timezone = resp["timezone"]
      print(f"Timezone : {timezone}")
      currency = resp["currency"]
      print(f"Currency : {currency}")
      isp = resp["isp"]
      print(f"ISP : {isp}")
      org = resp["org"]
      print(f"ORG : {org}")
      asp = resp["as"]
      print(f"AS : {asp}")
      aspname = resp["asname"]
      print(f"AS Name : {aspname}")
      reverse_lookup =  resp["reverse"]
      print(f"Reverse : {reverse_lookup}")
      mobile = str(resp["mobile"])
      print(f"Mobile : {mobile}")
      proxy_used = str(resp["proxy"])
      print(f"Proxy : {proxy_used}")
    
       



 #argparse start       
  
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
	'-maps','-m',dest='gmap',action='store_true',help='only shows the Google maps url'
	)

args = parser.parse_args()

#argparse stop
clear()
if not args.target:
    ip = input("\nIP/Url = ")
if args.target:
    ip = args.target
locate() #lets run it :D
