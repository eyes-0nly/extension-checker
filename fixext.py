#!/usr/bin/env python3
# coding=<utf-8>


import os
import argparse
import binascii

i = 0
e = 0
parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path to the directory")
args = parser.parse_args()
directory = args.path
os.chdir(directory)
for filename in filter(os.path.isfile, os.listdir(os.getcwd())):
    if filename != 'fixext.py':
        with open(filename, "rb") as binaryfile:
            binaryfile.seek(0)
            filetype = binaryfile.read(2)
            filetype = binascii.hexlify(filetype)
            extension = filename[filename.index('.'):]
        if filetype == b'8950' and extension != '.png':
            os.rename(filename, filename.replace(extension, ".png"))
            print('Extension of {} changed to png'.format(filename))
            e += 1
        elif filetype == b'ffd8' and extension != '.jpg':
            os.rename(filename, filename.replace(extension, ".jpg"))
            print('Extension of {} changed to jpg'.format(filename))
            e += 1
        elif filetype == b'4749' and extension != '.gif':
            os.rename(filename, filename.replace(extension, ".gif"))
            print('Extension of {} changed to gif'.format(filename))
            e += 1
        elif filetype == b'424d' and extension != '.bmp':
            os.rename(filename, filename.replace(extension, ".bmp"))
            print('Extension of {} changed to bmp'.format(filename))
            e += 1
        elif filetype == b'4949' and extension != '.tif':
            os.rename(filename, filename.replace(extension, ".tif"))
            print('Extension of {} changed to tif'.format(filename))
            e += 1
        elif filetype == b'4d4d' and extension != '.tiff':
            os.rename(filename, filename.replace(extension, ".tiff"))
            print('Extension of {} changed to tiff'.format(filename))
            e += 1
        i += 1
print('Done. {} Files. Fixed extensions {}'.format(i, e))
