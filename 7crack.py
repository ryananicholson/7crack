#!/usr/bin/python

# 7crack.py
# Description: Cracks Cisco Type 7 passwords
# Author: Ryan Nicholson (@ryananicholson)
# 
# Example: python 7crack.py --hash 095C4F1A0A1218000F

import argparse

def crackpassword(hashval):
    decrypt=lambda x:''.join([chr(int(x[i:i+2],16)^ord('dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87'[(int(x[:2])+i/2-1)%53]))for i in range(2,len(x),2)])
    plaintext = decrypt(hashval)
    print("Plaintext password is: " + plaintext)

# Argument handling
parser = argparse.ArgumentParser()
parser.add_argument("--hash", help="Cisco Type 7 Hash", required=True)
args = parser.parse_args()

crackpassword(args.hash)
