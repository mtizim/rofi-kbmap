#!/usr/bin/env python
import json
import os
import subprocess

LAUNCH_STR = "layout"


# get available layouts
options = (
    (next(x for x in os.popen("setxkbmap -query").read().split("\n") if "layout" in x))
    .split()[1]
    .split(",")
)

res = subprocess.getoutput(
    'echo "' + "\n".join(options) + f'" | rofi -i -dmenu -p {LAUNCH_STR}'
)
if any(res == option for option in options):
    # set res as the first choice
    langs = ",".join([res] + [option for option in options if option != res])
    os.popen(f"setxkbmap {langs}")
