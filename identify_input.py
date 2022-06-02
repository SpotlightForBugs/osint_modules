#!/bin/python3

##a module to get to know what kind of input is given##

import argparse
import re
import urllib.request
import tldextract
import ipaddress
import what3words
from verify_email import verify_email

parser=argparse.ArgumentParser()
parser.add_argument(
dest='input',help="the input, '_SPACE_' will be handled as spaces ' '"
)
args = parser.parse_args()

input_raw = args.input
input = input_raw.replace('_SPACE_',' ')




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
        
    regex_name = re.compile(r' ([a-zÄÖÜäöüß]+)( [a-zÄÖÜäöüß]+)*( [a-zÄÖÜäöüß]+)*$',re.IGNORECASE)
    is_name = regex_name.search(input)
  
    if is_name: 
        return True
          
    else: 
        return False
  



def is_username_on_well_known_pages():
    username_lookup_url = "https://knowem.com/checkusernames.php?u="+input
    open_lookup_url = urllib.request.urlopen(username_lookup_url)
    is_username_encrypted_output = open_lookup_url.read()

    username_resp = is_username_encrypted_output.decode("utf8")
    open_lookup_url.close()

    if "notavailable" in username_resp and not "but we ran into an error" in username_resp:
        return True
    else:
        return False

    
def is_email():
    email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(email_pattern,input):
          return True
    return False
        


#vars are False as standard
input_is_ip_address = False
input_is_url = False
input_is_w3w_address = False
input_is_first_and_last_name = False
input_is_username_on_well_known_pages = False
input_is_email = False


#end of vars

input_is_email = is_email()
input_is_ip_address = is_ip_address() #is it an ip address?
if input_is_ip_address == False:        #if not,
    if is_w3w_address() == True:        #is it a w3w address?
        input_is_w3w_address = True
    elif is_first_and_last_name() == True:
        input_is_first_and_last_name = True 
    elif input_is_email == False and is_url()  == True: #Do not check the subdoamins of the email-address
        input_is_url = True #only check for url if input is not something else to make the script faster
    elif is_username_on_well_known_pages() == True:
        input_is_username_on_well_known_pages = True #only check for url if input is not something else to make the script faster

        






print("reachable url >",input_is_url)
print("ip address >",input_is_ip_address)
print("w3w address >",input_is_w3w_address)
print("is first and lastname >",input_is_first_and_last_name)
print ("is an email-address >",input_is_email)
print("is username on well-known pages >",input_is_username_on_well_known_pages)












