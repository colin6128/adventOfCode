#!/usr/bin/env python

"""
Solution to Day1 of the 2018 Advent of code
@ https://adventofcode.com/2018/day/1
"""

import csv
from itertools import accumulate

### Part 1 of the puzzle ###

# Import text to python (converted to CSV)
path = 'Day1.csv'
data = []
frequency_total = 0

with open(path, newline='') as f:
    reader = csv.reader(f)
    ## data =[row for row in reader] #reads data from CSV file but only as strings
    # To import strings as integers into a list
    for row in reader:
        freq = int(row[0])
    
        data.append(freq)

        # print(data.count(freq)) # chk to see if works as expected. It does.

# print('# data =', len(data))

for i in data:
    frequency_total += i

print('The resulting frequency after all changes in frequency have been applied is:', frequency_total)

### Part 2 of the puzzle ###

data = data * 150
data.insert(0, 0)

# print(data)
# print('# data =', len(data))

accum_freq = []

for freqs in range(1, len(data) + 1):
    x = sum(data[:freqs])
    # print(x)
    accum_freq.append(x)
    # print(accum_freq.count(x))
    if accum_freq.count(x) > 1:
        # print('First repeated frequency is located at:',accum_freq.index(x))
        print('First repeated frequency is:', x)
        break
    
# print(accum_freq)
# print('# accum_freq =', len(accum_freq))

