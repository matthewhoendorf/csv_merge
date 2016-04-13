import sys
from sys import argv
from glob import glob

fout = open('output.csv','a') # output csv

for row in open(argv[1]): # first file
    fout.write(row)

for filename in argv[2:]: # second file through the last
    f = open(filename)
    f.next() # skip the header
    for row in f:
        fout.write(row)
    f.close()

fout.close()
