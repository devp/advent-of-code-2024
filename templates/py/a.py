#!/usr/bin/env python3

import csv
import sys

# DEFAULT_FILE_NAME = None
DEFAULT_FILE_NAME = 'sample'
# DEFAULT_FILE_NAME = 'input'

filename: str
if len(sys.argv) >= 2:
    filename = sys.argv[1]
elif DEFAULT_FILE_NAME is not None:
    filename = DEFAULT_FILE_NAME
else:
    sys.exit()

content = []

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        print(row)  # TODO
        content.append(row)

solution = len(content)

print(solution)
