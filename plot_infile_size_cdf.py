#!/usr/bin/env python

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]

data_points = []
headers = []

with open(filename, "r") as log:
    data = log.readlines()


infiles = {}

for line in data:
    infile_shorthash = line[line.find("(")+1:line.find(")")]
    infile_size = line.split("size: ")
    if len(infile_size) == 2:
        infile_size = int(infile_size[1])
        infiles[infile_shorthash] = infile_size
        #print(infile_shorthash + "--> " + "%d" % infile_size)


#plot CDF
fig, ax = plt.subplots(figsize=(8, 4))
x = infiles.values() 
x[:] = [i / 1024 for i in x] #KB
n_bins = len(x)
print len(x)
n, bins, patches = ax.hist(x, n_bins, normed=1, histtype='step',
                           cumulative=True, label='gg-mosh')
ax.legend(loc='right')
ax.set_title('Data file size distribution')
ax.set_xscale('log') #,nonposx='clip')
ax.set_xlabel('Input File size (KB)')
ax.set_xlim(0,max(x))
ax.set_ylim(0,1)
ax.set_ylabel('CDF')

plt.show()

#data_points.sort(key=lambda x: x[0])

#T0 = data_points[0][0]

#for d in data_points:
#    d[0] = d[0] - T0
#    d.append(sum(d))

#print("\t".join(["#"] + headers))
#for i, d in enumerate(data_points):
#    print("\t".join([str(i)] + [str(x) for x in d]))
