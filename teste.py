#!/usr/bin/python3

import csv

nms = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]

f = open('numbers3.csv', 'w')

with f:

    writer = csv.writer(f)
    writer.writerows(nms)