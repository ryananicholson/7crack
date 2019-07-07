#!/usr/bin/python

import argparse

def crackpassword(hashval):
	crypttext = hashval.upper()
	print(crypttext)

# Argument handling
parser = argparse.ArgumentParser()
parser.add_argument("--hash", help="Cisco Type 7 Hash", required=True)
args = parser.parse_args()

crackpassword(args.hash)