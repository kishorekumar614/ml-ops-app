#!/bin/bash
set -e
docker run -d --name student-app -p 80:5000 student-app
