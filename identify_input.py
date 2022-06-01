#!/bin/python3

##a module to get to know what kind of input is given##

import argparse
import re
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
    
def is_first_and_last_name():
    
  
    
    regex_name = re.compile(r' ([a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)
    res = regex_name.search(input)
  
    if res: 
        return True
          
    else: 
        return False
  


#vars are False as standard
input_is_ip_address = False
input_is_url = False
input_is_w3w_address = False
input_is_first_and_last_name = False




#end of vars

input_is_ip_address = is_ip_address() #is it an ip address?
if input_is_ip_address == False:        #if not,
    if is_w3w_address() == True:        #is it a w3w address?
        input_is_w3w_address = True
    if is_first_and_last_name() == True:
        input_is_first_and_last_name = True 
    else:
        input_is_url = is_url() #only check for url if input is not something else to make the script faster







print("reachable url : "+input_is_url)
print("ip address: "+input_is_ip_address)
print("w3w address: "+input_is_w3w_address)
print("is first and lastname",input_is_first_and_last_name)
 











