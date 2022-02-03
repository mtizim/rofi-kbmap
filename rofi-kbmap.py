#!/usr/bin/env python
import json
import os
import subprocess

LAUNCH_STR = "layout"


# get available layouts
options = "\n".join(
    (next(x for x in os.popen("setxkbmap -query").read().split("\n") if "layout" in x))
    .split()[1]
    .split(",")
)
res = subprocess.getoutput('echo "' + options + f'" | rofi -i -dmenu -p {LAUNCH_STR}')
langs = ",".join([res] + [option for option in options.split("\n") if option != res])

# set res as the first choice
os.popen(f"setxkbmap {langs}")
