#!/bin/python3

##a module to get to know what kind of input is given##

import argparse
import urllib.request
import tldextract
import ipaddress
import what3words

parser=argparse.ArgumentParser()
parser.add_argument(
dest='input'
)
args = parser.parse_args()

input_raw = args.input
input = input_raw



w3w_api_key = "62JXOCMQ" #Public API,replace with your own
geocoder = what3words.Geocoder(w3w_api_key)

def is_url(): 
  

    url = input
    parsed = tldextract.extract(url)
    domain_without_proto = parsed.domain + '.' + parsed.suffix
    domain = 'http://' + domain_without_proto
    try:
        http_status = urllib.request.urlopen(domain).getcode()
     
        if http_status == 200:
            return True
    except:
            return False


def is_ip_address():
    try:
        ip = ipaddress.ip_address(input)
        return True
    except ValueError:
        return False
    
def is_w3w_address():
    w3w_res = geocoder.convert_to_coordinates(input)
    if "error" in w3w_res:
        return False
    else:
        return True
    
    


#vars are False as standard
input_is_ip_address = False
input_is_url = False
input_is_w3w_address = False




#end of vars

input_is_ip_address = is_ip_address()
if input_is_ip_address == False:
    if is_w3w_address() == True:
        input_is_w3w_address = True
    else:
        input_is_url = is_url() #only check for url if input is not an ip address to make the script faster


print("reachable url : "+input_is_url)
print("ip address: "+input_is_ip_address)
print("w3w address: "+input_is_w3w_address)
 











