#!/usr/bin/python

# 7crack.py
# Description: Cracks Cisco Type 7 passwords
# Author: Ryan Nicholson (@ryananicholson)
# 
# Example: python 7crack.py --hash 095C4F1A0A1218000F

import argparse

def crackpassword(hashval):
	constant = "tfd;kfoA,.iyewrkldJKD"
	ciphertext = hashval.upper()
	seed = int(ciphertext[0] + ciphertext[1])
	plaintext = ""

	for i in range(1, len(ciphertext) / 2):
		salt = constant[seed - 1]
		hexval = int(ciphertext[i * 2] + ciphertext[i * 2 + 1], 16)
		plaintext += chr(hexval ^ ord(salt))
		seed += 1

	print("Plaintext password is: " + plaintext)

# Argument handling
parser = argparse.ArgumentParser()
parser.add_argument("--hash", help="Cisco Type 7 Hash", required=True)
args = parser.parse_args()

crackpassword(args.hash)