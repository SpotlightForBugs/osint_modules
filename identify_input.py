#!/bin/python3

##a module to get to know what kind of input is given##

import argparse
import urllib.request
import tldextract
import ipaddress

parser=argparse.ArgumentParser()
parser.add_argument(
dest='input'
)
args = parser.parse_args()

input_raw = args.input
input = input_raw






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
    

input_is_url = is_url()
input_is_ip_address = is_ip_address()

print(input_is_url,input_is_ip_address) 











