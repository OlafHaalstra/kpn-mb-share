#!/bin/bash

# Start the run once job.
echo "Docker container has been started"

# Setup a cron schedule
echo "5 * 1 * * sh /app/run.sh > /dev/stdout
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
crond -f