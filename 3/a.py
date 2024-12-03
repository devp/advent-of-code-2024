#!/usr/bin/env python3

import sys
import re

# DEFAULT_FILE_NAME = None
# DEFAULT_FILE_NAME = 'sample'
DEFAULT_FILE_NAME = 'input'

filename: str
if len(sys.argv) >= 2:
    filename = sys.argv[1]
elif DEFAULT_FILE_NAME is not None:
    filename = DEFAULT_FILE_NAME
else:
    sys.exit()

data = None
with open(filename) as open_file:
    data = open_file.read()

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
mult_args = [
    tuple(
        int(s)
        for s in re.sub(r".*\((\d+,\d+)\)", r"\1", m).split(",")
    )
    for m in matches
]
sums = sum([x * y for (x, y) in mult_args])

solution = sums

print(solution)
