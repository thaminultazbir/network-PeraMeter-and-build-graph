import os
import sys

def ip_file_valid():
    ip_file = input("Enter the Ip File Path and Name: ")

    if os.path.isfile(ip_file):
        print("IP file is valid")
    
    else:
        print("IP file is Invalid! Please Check and try again")
        sys.exit()
    

    selected_ip_file = open("ip_file", 'r')
    selected_ip_file.seek(0)
    ip_list = selected_ip_file.readlines()
    selected_ip_file.close()
    return ip_list