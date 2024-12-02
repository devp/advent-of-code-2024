#!/usr/bin/env python3

import csv
import sys

filename = sys.argv[1]

list_a = []
list_b = []

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        (a,b) = row
        list_a.append(int(a))
        list_b.append(int(b))

list_a = sorted(list_a)
list_b = sorted(list_b)

total_dist = 0

for (i, a) in enumerate(list_a):
    b = list_b[i]
    dist = abs(a - b)
    total_dist += dist

print(total_dist)
