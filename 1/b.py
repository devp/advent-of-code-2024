#!/usr/bin/env python3

import csv
import sys

filename = sys.argv[1]

list_a = []
counts_b = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for (a,b) in csv_reader:
        list_a.append(int(a))
        if b in counts_b:
            counts_b[b] += 1
        else:
            counts_b[b] = 1

total_dist = 0

for (i, a) in enumerate(list_a):
    k = str(a)
    b_count = counts_b[k] if k in counts_b else 0
    dist = a * b_count
    total_dist += dist

print(total_dist)
