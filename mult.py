#!/usr/bin/python2

import argparse
import sys

parser = argparse.ArgumentParser(description='Process some numbers.')
args = parser.parse_args()

Product = 1.0
Flag = 0

try:
    for Line in iter(sys.stdin.readline, ''):
        if(Line == '\n'):
            if(Flag == 1):
                print "Product is " + str(Product)
            else:
                print "Error: No terms to calculate"
            print
            Product = 1
            Flag = 0
        else:
            Product = Product * float(Line)
            Flag = 1
    if(Flag == 1):
        print "Product is " + str(Product)
    else:
        print "Error: No terms to calculate"
except: # Global catch
    print "Error: product calculation failure, check args"
    sys.exit(1)

