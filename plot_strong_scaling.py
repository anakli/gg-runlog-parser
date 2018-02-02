import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


plt.style.use('default')
plt.rcParams.update({'font.size': 24})
plt.rcParams['errorbar.capsize'] = 2


#gg-cmake with Redis c4.8xlarge
n = [1, 2, 10, 25, 50, 75, 100, 1000]
runtime = [726, 419, 140.8, 50.2, 66.35, 31.9, 28.2, 25.5]
io_perc = [6, 8.3, 5.03, 5.24, 7.5, 6.2, 6.14, 11.3]

#gg-ffmpeg with Redis c4.8xlarge
#n = [1, 10, 25, 50, 75, 100, 1000]
#runtime = [726, 140.8, 50.2, 66.35, 31.9, 28.2, 25.5]
#io_perc = [6, 5.03, 5.24, 7.5, 6.2, 6.14, 11.3]

fig, ax1 = plt.subplots(1,1, figsize=(15,8))
#fig, ax1 = plt.subplots()
ax1.plot(n, runtime, 'b-')
ax1.set_xlabel('# workers')
ax1.set_xscale('log', basex=10)
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Job Runtime (s)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(n, io_perc, 'r--')
ax2.set_ylabel('IO time %', color='r')
ax2.set_ylim(0,100)
ax2.tick_params('y', colors='r')


for axis in [ax1.xaxis, ax1.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
for axis in [ax2.xaxis, ax2.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

fig.tight_layout()
fig.savefig("gg-strong-scaling-runtime-iotime.pdf")
plt.show()
