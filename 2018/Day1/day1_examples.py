#!/usr/bin/env python

"""
Solution to Day1 of the 2018 Advent of code
@ https://adventofcode.com/2018/day/1 using example 1 to check it.
"""

from itertools import accumulate

### Part 1 of the puzzle ###
# data = [1, -2, 3, 1]      # first reaches 2 twice
# data = [1, -1]              # first reaches 0 twice
# data = [3, 3, 4, -2, -4]    # first reaches 10 twice
# data = [-6, 3, 8, 5, -6]    # first reaches 5 twice
data = [7, 7, -2, -7, -4]    # first reaches 14 twice

frequency_total = 0

for i in data:
    frequency_total += i

print('The resulting frequency after all changes in frequency have been applied is:', frequency_total)

# print('# data =', len(data))

data = data * 4
data.insert(0, 0)

# print(data)
# print('# data =', len(data))

### Part 2 of the puzzle ###

accum_freq = []

for freqs in range(1, len(data) + 1):
    x = sum(data[:freqs])
    # print(x)
    accum_freq.append(x)
    # print(accum_freq.count(x))
    if accum_freq.count(x) > 1:
        # print('First repeated frequency is located at index:',accum_freq.index(x))
        print('First repeated frequency is:', x)
        break            

# print(accum_freq)
# print('# accum_freq =', len(accum_freq))

