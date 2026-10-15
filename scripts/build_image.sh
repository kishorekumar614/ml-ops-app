#!/bin/bash
set -e
cd /home/ec2-user/app
docker build -t student-app .
