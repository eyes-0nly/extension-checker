#!/usr/bin/env python3
# coding=<utf-8>


import os
import binascii

i = 0
e = 0
print("Enter the path to the directory:", end=" ")
directory = input()
os.chdir(directory)
for filename in os.listdir(os.getcwd()):
    if filename != 'rename.py':
        with open(filename, "rb") as binaryfile:
            binaryfile.seek(0)
            filetype = binaryfile.read(2)
            filetype = binascii.hexlify(filetype)
            extension = filename[-4:]
        if filetype == b'8950' and extension != '.png':
            os.rename(filename, filename.replace(filename[-4:], ".png"))
            print('Extension of {} changed to png'.format(filename))
            e += 1
        elif filetype == b'ffd8' and extension != '.jpg':
            os.rename(filename, filename.replace(filename[-4:], ".jpg"))
            print('Extension of {} changed to jpg'.format(filename))
            e += 1
        elif filetype == b'4749' and extension != '.gif':
            os.rename(filename, filename.replace(filename[-4:], ".gif"))
            print('Extension of {} changed to gif'.format(filename))
            e += 1
        i += 1
print('Done. {} Files. Changed extensions {}'.format(i, e))
