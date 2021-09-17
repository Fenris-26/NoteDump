#!/usr/bin/env python3

import os.path
import re
import sqlite3
import sys

FAIL = '\033[91m'
WARNING = '\033[93m'
END = '\033[0m'
Usage = f"{WARNING}Usage: {sys.argv[0]} <Sticky Notes DB Path>{END}"

if(len(sys.argv) > 1):
    db = sys.argv[1]
else:
    db = str(os.environ.get(
        'LOCALAPPDATA')) + '\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite'

if(not os.path.isfile(db)):
    if(len(sys.argv) > 1):
        raise SystemExit(
            f"{FAIL}Could not find the specified DB\n\n{Usage}")
    else:
        raise SystemExit(
            f"{FAIL}Could not find a local Sticky Notes DB\n\n{WARNING}Try to manually specify its path\n{Usage}")

try:
    conn = sqlite3.connect(db)
except:
    raise SystemExit(f"{FAIL}Could not connect to the Sticky Notes DB{END}")

query = conn.cursor().execute('select Text from Note')
for index, row in enumerate(query, start=1):
    print(f"Note {index}:")
    for line in row[0].split('\n'):
        print(re.sub('id=[a-z0-9-]*', '', line)[2:])
    print()
