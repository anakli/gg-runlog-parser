#!/bin/bash -ex

aws s3 rm --recursive s3://${GG_S3_BUCKET?"GG_S3_BUCKET not set"}/runlogs/
