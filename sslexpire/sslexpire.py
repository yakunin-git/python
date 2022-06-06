#!/usr/bin/python3.8

import socket
import ssl
import datetime
import argparse
import json

def ssl_expiry_datetime(hostname):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    conn.settimeout(3.0)
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    return datetime.datetime.strptime(ssl_info["notAfter"], ssl_date_fmt)

def ssl_valid_time_remaining_number(hostname):
    expires = ssl_expiry_datetime(hostname)
    delta = expires - datetime.datetime.utcnow()
    return delta.days

def ssl_valid_time_remaining_human(hostname):
    expires = ssl_expiry_datetime(hostname)
    return expires - datetime.datetime.utcnow()

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="Output number only", action="store_true")
parser.add_argument("-j", "--json", help="Output in json format", action="store_true")
parser.add_argument("domain_name")
args = parser.parse_args()

if args.number:
    print(ssl_valid_time_remaining_number(args.domain_name))
elif args.json:
    print(json.dumps({args.domain_name: int(ssl_valid_time_remaining_number(args.domain_name)),
                      "domain": args.domain_name,
                      "expire": int(ssl_valid_time_remaining_number(args.domain_name))},
                     sort_keys=False, indent=3))
else:
    print(ssl_valid_time_remaining_human(args.domain_name))
