#!/usr/bin/env python

"""Program: SSH from Python
Programmer: Michael Fryar, Research Fellow, EPoD
Date created: August 28, 2017

Purpose: Establish SSH tunnel using python rather than bash
"""

import os
import subprocess

from write_to_gsheets_AGG import write_to_sheet

# Change to directory containing configuration files
os.chdir("C:/Users/mifryar/Documents/epodx")

# Establish ssh tunnel in background that auto-closes
# -f "fork into background", -F "use configuration file"
# -o ExistOnForwardFailure=yes "wait until connection and port
#   forwardings are set up before placing in background"
# sleep 10 "give python script 60 seconds to start using tunnel and
#   close tunnel after python script stops using it"
# Ref 1: https://www.g-loaded.eu/2006/11/24/auto-closing-ssh-tunnels/
# Ref 2: https://gist.github.com/scy/6781836

config = "-F ./ssh-config epodx-analytics-api"
option = "-o ExitOnForwardFailure=yes"

ssh = subprocess.run("ssh -f config option sleep 60")

# Change to directory containing script to write to Google Sheets
os.chdir("C:/Users/mifryar/Documents/epodx-dashboards")
write_to_sheet()