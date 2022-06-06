#!/usr/bin/python3.8

import argparse
import pyAesCrypt
import getpass
import os


def get_password():
    aes_password_first = getpass.getpass("Enter password: ")
    aes_password_second = getpass.getpass("Enter password again: ")

    if aes_password_first == aes_password_second:
        return aes_password_second
    else:
        print("The entered password does not match, please try again...")
        exit(1)


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--clean", help="Delete source file", action="store_true")
parser.add_argument("-e", "--encrypt", help="Encrypting file", action="store_true")
parser.add_argument("-d", "--decrypt", help="Decrypting file", action="store_true")
parser.add_argument("file")
args = parser.parse_args()

if args.file:
    print("The file you have chosen: " + args.file)
    if not os.path.exists(args.file):
        print("The file does not exist or the path entered is incorrect.")
        exit(1)

if args.encrypt:
    print("The file: " + args.file + " will be encrypted.")
    try:
        pyAesCrypt.encryptFile(args.file, args.file + ".aes", get_password())
        if args.clean:
            os.system('rm ' + args.file)
    except ValueError as encrypting_error:
        print("An error occurred while encrypting the file.")
        print(encrypting_error)
        exit(1)
    else:
        print("File encrypted successfully.")
        exit(0)

if args.decrypt:
    print("The file: " + args.file + " will be decrypted.")
    try:
        pyAesCrypt.decryptFile(args.file, args.file.replace('.aes', ''), get_password())
        if args.clean:
            os.system('rm ' + args.file)
    except ValueError as decrypt_error:
        print("An error occurred while decrypting the file.")
        print(decrypt_error)
        exit(1)
    else:
        print("File decrypted successfully.")
        exit(0)

file_options = input("Enter E/D for encrypt or decrypt file: ")

if file_options == "E":
    print("The file: " + args.file + " will be encrypted.")
    try:
        pyAesCrypt.encryptFile(args.file, args.file + ".aes", get_password())
        if args.clean:
            os.system('rm ' + args.file)
    except ValueError as encrypting_error:
        print("An error occurred while encrypting the file.")
        print(encrypting_error)
        exit(1)
    else:
        print("File encrypted successfully.")
elif file_options == "D":
    print("The file: " + args.file + " will be decrypted.")
    try:
        pyAesCrypt.decryptFile(args.file, args.file.replace('.aes', ''), get_password())
        if args.clean:
            os.system('rm ' + args.file)
    except ValueError as decrypt_error:
        print("An error occurred while decrypting the file.")
        print(decrypt_error)
        exit(1)
    else:
        print("File decrypted successfully.")
else:
    print("You entered incorrect values, please try 'E' for encrypt, or 'D' for decrypt.")
