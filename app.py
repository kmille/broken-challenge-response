#!/usr/bin/env python3

import sys
import os
from hashlib import md5
from binascii import hexlify

# socat tcp-l:2023,reuseaddr,fork exec:'python app.py'

flag = "MRMCD18{123123123}"
shared_secret = "838385723752375832975983275832659326598326535932653261324398247" 


def create_response(challenge):
    challenge = challenge.strip()
    response =  md5(shared_secret.encode() + challenge.encode()).digest()
    return hexlify(response).decode()


def main():
    sys.stdout.write("Hey. You need to authenticate to get the flag. We will do a simple challenge response with a shared key. "
                     "You know the shared key do you?\n"
                     "Let me authenticate first. Give me your challenge\n")
    sys.stdout.flush()
    challenge = sys.stdin.readline()
    response = create_response(challenge)
    challenge = hexlify(os.urandom(10)).decode()
    sys.stdout.write(f"Response: {response}\n"
                     f"Please authenticate with md5(shared_secret, challenge). Your Challenge is {challenge}\n")
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    if create_response(challenge) == response:
        sys.stdout.write(f"Welcome. Here is the flag {flag}\n")
    else:
        sys.stdout.write("Authentication failed\n")
    sys.stdout.flush()


if __name__ == '__main__':
    main()
