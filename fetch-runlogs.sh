#!/bin/bash -ex

mkdir -p $1
aws s3 cp --recursive s3://${GG_S3_BUCKET?"GG_S3_BUCKET is not set"}/runlogs $1/
