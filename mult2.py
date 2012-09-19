#!/usr/bin/python2

import argparse
import sys
import fileinput

parser = argparse.ArgumentParser(description='Process some numbers.')
parser.add_argument('inFile', nargs='*', metavar='file')
parser.add_argument('--ignore-blank numbers', dest="BlankFlag", help="Ignores blank lines in input")
parser.add_argument('--ignore-non-numeric bad_numbers', dest="NumericFlag", help="Ignores lines without numeric input")
args = parser.parse_args()
                   
Product = 1.0
Flag = 0

for Line in fileinput.input(args.inFile):
    if(Line == '\n'):
        if(not args.BlankFlag):
            if(Flag == 1):
                print "Product is " + str(Product)
            else:
                sys.stderr.write("Error: No terms to calculate")
            print
            Product = 1
            Flag = 0
    else:
        if(not args.NumericFlag):
            try:
                Product = Product * float(Line)
                Flag = 1
            except: # Global catch
                sys.stderr.write("Error: product calculation failure, check args")
                sys.exit(1)
        else:
            try:
                Product = Product * float(Line)
                Flag = 1
            except:
                Product = Product
if(Flag == 1):
    print "Product is " + str(Product)
else:
    sys.stderr.write("Error: No terms to calculate")

sys.exit(0)

