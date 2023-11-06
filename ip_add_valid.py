import sys

def ip_addr_valid(list):
    for ip in list:
        ip = ip.rstrip("\n")
        ip_octet = ip.split(".")