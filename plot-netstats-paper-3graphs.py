#!/usr/bin/env python

import os
import sys
import numpy as np 
from io import StringIO 
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

plt.style.use('default')
plt.rcParams.update({'font.size': 24})
plt.rcParams['errorbar.capsize'] = 2

# python plot-netstats.py gg-cmake-s3netstats-1000lambdas-REDO sort100GB-500worker-netstatsTX video3-4k-b50-s3-rxstats.txt

datadir = sys.argv[1]
netstat_dir = os.path.join(datadir, "netstats")
rxfilename = "rxstats.txt"
txfilename = "txstats.txt"


rxstats = open(os.path.join(netstat_dir, rxfilename), 'r')
txstats = open(os.path.join(netstat_dir, txfilename), 'r')

i = 0
xmax = 0
xmin = 0
ytotal = None
DURATION = 20 #15
for line in rxstats:
	data = np.loadtxt(StringIO(unicode(line)), delimiter='\t') 
	start_time = int(data[1])
	if i == 0 :
		xmin = start_time
		xmax = xmin + DURATION
 	i += 1
	x = np.array(range(start_time, start_time + len(data) - 2))
	y = np.delete(data, [0,1])
	#plt.fill_between(x, y_prev, y, facecolor="#CC6666", alpha=.7)
	#y_prev = y
        if len(data) <= 2:
            continue
        #print x, x[0], xmin, line
	
	#plt.plot(x,y)
	padzeros = x[0] - xmin
	if padzeros > 0:
		y = np.pad(y, (padzeros,0), "constant", constant_values=(0,0))
	padend = xmax - x[-1]
	if padend > 0:
		y = np.pad(y, (0,padend), "constant" , constant_values=(0,0))
	if ytotal is not None:
		ytotal = np.row_stack((ytotal,y))
	else:
		ytotal = y
		#ytotal = np.row_stack((np.zeros(DURATION+1),y))
	
scale_y = 1e9
x = range(0, xmax - xmin +1)
ycum = np.cumsum(ytotal, axis=0)
workers = np.count_nonzero(ytotal, axis=0)
workers[workers==0] = 1
GG_CAPACITY = .85
ysum = np.sum(ytotal, axis=0)  / scale_y /GG_CAPACITY #cumulative throughput/capacity
#yavg = ysum/workers  #individual throughput/capacity

#fig = plt.figure()
fig, (ax,ax2, ax3) = plt.subplots(3,1, figsize=(18,12))
#ax = fig.add_subplot(111)
BYTES_TO_BITS=8
#ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*BYTES_TO_BITS/scale_y))
#ax.yaxis.set_major_formatter(ticks_y)
#ax.plot(x, np.transpose(ycum))
#ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_y/0.85))
#ax.yaxis.set_major_formatter(ticks_y)
gg  = ax.plot(x, np.transpose(ysum), label='gg-cmake-650workers', linewidth=3)
#ax.plot(x, np.transpose(yavg))
#ax.legend([gg], ['gg-cmake-650workers'])
ax.legend(loc='upper right')


datadir = sys.argv[2]
netstat_dir = os.path.join(datadir, "netstats")
rxfilename = "rxstats.txt"


rxstats = open(os.path.join(netstat_dir, rxfilename), 'r')

i = 0
xmax = 0
xmin = 0
ytotal = None
DURATION = 300 #15
for line in rxstats:
	data = np.loadtxt(StringIO(unicode(line)), delimiter='\t') 
	start_time = int(data[1])
	if i == 0 :
		xmin = start_time
		xmax = xmin + DURATION
 	i += 1
	x = np.array(range(start_time, start_time + len(data) - 2))
	y = np.delete(data, [0,1])
	#plt.fill_between(x, y_prev, y, facecolor="#CC6666", alpha=.7)
	#y_prev = y
        if len(data) <= 2:
            continue
        #print x, x[0], xmin, line

	#plt.plot(x,y)
	padzeros = x[0] - xmin
	if padzeros > 0:
		y = np.pad(y, (padzeros,0), "constant", constant_values=(0,0))
	padend = xmax - x[-1]
	if padend > 0:
		y = np.pad(y, (0,padend), "constant" , constant_values=(0,0))
	if ytotal is not None:
		ytotal = np.row_stack((ytotal,y))
	else:
		ytotal = y
		#ytotal = np.row_stack((np.zeros(DURATION+1),y))
	
x = range(0, xmax - xmin +1)
ycum = np.cumsum(ytotal, axis=0)
workers = np.count_nonzero(ytotal, axis=0)
workers[workers==0] = 1
SORT_CAPACITY=100
ysum = np.sum(ytotal, axis=0) / scale_y / SORT_CAPACITY #cumulative throughput/capacity
#yavg = ysum/workers  #individual throughput/capacity

#fig = plt.figure()
#fig, ax = plt.subplots(1,1, figsize=(15,8))
#ax = fig.add_subplot(111)
scale_y = 1e9
BYTES_TO_BITS=8
#ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*BYTES_TO_BITS/scale_y))
#ax.yaxis.set_major_formatter(ticks_y)
#ax.plot(x, np.transpose(ycum))
#ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_y/100))
#ax.yaxis.set_major_formatter(ticks_y)
sort = ax2.plot(x, np.transpose(ysum), label='Sort100GB-500workers', color='#2ca02c', linewidth=3)
ax2.set_xlim(0, 30)
ax2.set_ylim(0, 0.1)
ax2.set_xlabel("Time (s)")
#ax2.set_ylabel("Total GB/s per GB capacity")
#ax.set_title("RX network utilization")
ax2.legend(loc='upper right')



rxfilename = sys.argv[3]
rxstats = open(rxfilename, 'r')

i = 0
xmax = 0
xmin = 0
ytotal = None
DURATION = 200 #15
for line in rxstats:
	data = np.loadtxt(StringIO(unicode(line)), delimiter='\t') 
	start_time = int(data[1])
	if i == 0 :
		xmin = start_time
		xmax = xmin + DURATION
 	i += 1
	x = np.array(range(start_time, start_time + len(data) - 2))
	y = np.delete(data, [0,1])
	#plt.fill_between(x, y_prev, y, facecolor="#CC6666", alpha=.7)
	#y_prev = y
        if len(data) <= 2:
            continue
        #print x, x[0], xmin, line

	#plt.plot(x,y)
	padzeros = x[0] - xmin
	if padzeros > 0:
		y = np.pad(y, (padzeros,0), "constant", constant_values=(0,0))
	padend = xmax - x[-1]
	if padend > 0:
		y = np.pad(y, (0,padend), "constant" , constant_values=(0,0))
	if ytotal is not None:
		ytotal = np.row_stack((ytotal,y))
	else:
		ytotal = y
		#ytotal = np.row_stack((np.zeros(DURATION+1),y))
	
x = range(0, xmax - xmin +1)
ycum = np.cumsum(ytotal, axis=0)
workers = np.count_nonzero(ytotal, axis=0)
workers[workers==0] = 1
VIDEO_CAPACITY=0.3
ysum = np.sum(ytotal, axis=0) / scale_y / VIDEO_CAPACITY #cumulative throughput/capacity
#yavg = ysum/workers  #individual throughput/capacity

#fig = plt.figure()
#fig, ax = plt.subplots(1,1, figsize=(15,8))
#ax = fig.add_subplot(111)
scale_y = 1e9
BYTES_TO_BITS=8
#ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*BYTES_TO_BITS/scale_y))
#ax.yaxis.set_major_formatter(ticks_y)
#ax.plot(x, np.transpose(ycum))
#ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_y/100))
#ax.yaxis.set_major_formatter(ticks_y)
sort = ax3.plot(x, np.transpose(ysum), label='video-analytics-500workers', color='#ff7f0e', linewidth=3)
ax3.set_xlim(0, 10)
#a32.set_ylim(0, 0.1)
ax3.set_xlabel("Time (s)")
#ax2.set_ylabel("Total GB/s per GB capacity")
#ax.set_title("RX network utilization")
ax3.legend(loc='upper right')




rxstats.close()
#plt.show()
fig.text(0.02, 0.5, 'Total GB/s per GB capacity', ha='center', va='center', rotation='vertical')
fig.tight_layout()
fig.savefig("throughput-per-capacity.pdf")
plt.show()
exit(0)

i = 0
xmax = 0
xmin = 0
ytotal = None
for line in txstats:
	data = np.loadtxt(StringIO(unicode(line)), delimiter='\t') #, np.array(line)
	start_time = int(data[1])
	if i == 0 :
		xmin = start_time
		xmax = xmin + DURATION
 	i += 1
	x = np.array(range(start_time, start_time + len(data) - 2))
	y = np.delete(data, [0,1])
	#plt.fill_between(x, y_prev, y, facecolor="#CC6666", alpha=.7)
	#y_prev = y
        if len(data) <= 2:
            continue
	
	#plt.plot(x,y)
	padzeros = x[0] - xmin
	if padzeros > 0:
		y = np.pad(y, (padzeros,0), "constant", constant_values=(0,0))
	padend = xmax - x[-1]
	if padend > 0:
		y = np.pad(y, (0,padend), "constant" , constant_values=(0,0))

	if ytotal is not None:
		ytotal = np.row_stack((ytotal,y))
	else:
		ytotal = y
		#ytotal = np.row_stack((np.zeros(DURATION+1),y))
	
x = range(0, xmax - xmin +1)
ycum = np.cumsum(ytotal, axis=0)
fig = plt.figure()
ax = fig.add_subplot(111)
scale_y = 1e9
BYTES_TO_BITS=8
ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*BYTES_TO_BITS/scale_y))
ax.yaxis.set_major_formatter(ticks_y)
ax.plot(x, np.transpose(ycum))

ax.set_xlabel("Time (s)")
ax.set_ylabel("Cumulative Gb/s")
ax.set_title("TX network utilization")

plt.show()
txstats.close()
