#!/usr/bin/env python3
'''
project-euler-offline.py
Christopher Su
Checks solutions to Project Euler problems offline.
'''

import base64
import json
import logging
import sys

from Crypto.Cipher import AES

MASTER_KEY = "03b5660c7c16a07bovIddIdhi4OxUcGinph"


def loadJSON(jsonStr):
    try:
        data = json.loads(jsonStr)
    except ValueError:
        logging.exception("Error parsing:\n%s" % jsonStr)
        sys.exit(1)
    return data


def decrypt_val(cipher_text):
    dec_secret = AES.new(MASTER_KEY[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text)).decode("utf-8")
    clear_val = raw_decrypted.rstrip("\0")
    return clear_val


def main():
    with open("./solutions-encrypted", "r") as fh:
        txtStr = fh.read()
    plain_text = decrypt_val(txtStr)
    solutions = loadJSON(plain_text)

    current = input("What problem are you currently working on? ")

    while True:
        proposed = input("\nEnter solution: ")
        if proposed == "exit":
            break
        elif proposed == solutions[current]:
            print("Correct!")
            current = input("\nWhat problem are you working on? ")
            if current == "exit":
                break
        else:
            print("Sorry, that is incorrect.")

if __name__ == "__main__":
    main()
