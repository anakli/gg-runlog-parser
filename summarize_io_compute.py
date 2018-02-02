import numpy as np
import pandas as pd
import os
import sys


filename = sys.argv[1]
data = pd.read_csv(filename, sep="\t", header=None)
data.columns = [ "worker", "start-time", "disk-write", "copy-executables", "fetch-deps", "execute", "check-outfile", "upload-outfile", "end-time" ]

#print "upload times:\n" , data.loc[:,"upload-outfile"] 
#print "fetch times:\n" , data.loc[:,"fetch-deps"] 
fetch = data["fetch-deps"].sum()
compute = data["execute"].sum()
upload = data["upload-outfile"].sum() + data["check-outfile"].sum()
total = fetch + compute + upload
print "Total fetch time:" , fetch, " (", fetch/total * 100, "%)"
print "Total exec time:" , compute, " (", compute/total * 100, "%)"
print "Total upload time:" , upload, " (", upload/total * 100, "%)"
print "Total lambda time:", total
print "IO time: ", (fetch+upload)/total * 100, "%, Compute time: ", compute/total * 100, "%"

print "Total job runtime:" , data["end-time"].iloc[-1]
