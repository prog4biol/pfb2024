#!env/bin/bash python3

#Problem set 10, number 7
# Pipelines:
# a. Create a script that runs a command with subprocess.run.
# b. Check the exit status
# c. If exit status is good, run a second command.

import subprocess

rtn = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE )  # specify you want to capture STDOUT
bytes = rtn.stdout
#print(bytes)
stdout = bytes.decode('utf-8')
# something like
lines = stdout.splitlines()
print(lines)