#!/usr/bin/env python

import os
import sys
import redis

datadir = sys.argv[1]

if not os.path.exists(datadir):
    os.makedirs(datadir)

r = redis.StrictRedis(host=os.environ['GG_REDIS_HOSTADDR'], port=6379, db=0)
runlog_keys = r.keys(pattern="runlogs*")

for key in runlog_keys:
    f = open(os.path.join(datadir,key.split("runlogs/")[1]), 'w+')
    f.write(r.get(key))

