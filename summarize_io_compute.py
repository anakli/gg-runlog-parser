#!/usr/bin/env python

import numpy as np
import pandas as pd
import os
import sys


filename = sys.argv[1]
data = pd.read_csv(filename, sep="\t", header=None)
data.columns = [ "worker", "start-time", "disk-write", "copy-executables", "fetch-deps", "execute", "check-outfile", "upload-outfile", "end-time" ]

print "upload times:\n" , data.loc[:,"upload-outfile"] 
#print "fetch times:\n" , data.loc[:,"fetch-deps"] 
print "Total fetch time:" , data["fetch-deps"].sum()
print "Total exec time:" , data["execute"].sum()
print "Total upload time:" , data["upload-outfile"].sum() + data["check-outfile"].sum()
