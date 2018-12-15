#!/usr/bin/env python

"""
Solution to Day2 of the 2018 Advent of code
@ https://adventofcode.com/2018/day/2.
"""
### Puzzle part 1 ###
# set variables
data = []
two_letter = 0
three_letter = 0

# form a list of entries
path = 'Day2.txt'
try:
    with open(path, newline='\n') as f:
        for line in f:
            line = line.replace('\n', '')
            data.append(line)
except FileNotFoundError:
    f = ""

# print(data) # debug chk for import of lines
# print(len(data))

# create checksum
# calculate how many entries have 2 letters the same
for i in range(0, len(data)):

    # calculate how many have 2 letters the same
    for letter in data[i]:
        data[i].count(letter)
        if data[i].count(letter) == 2:
            # print('2 found') # debug chk
            two_letter += 1
            break # only count once per entry

    # calculate how many have 3 letters the same
    for letter in data[i]:
        if data[i].count(letter) == 3:
            # print('3 found') # debug chk
            three_letter += 1
            break # only count once per entry

# Calculate answer to part one
# print(two_letter, three_letter)
checksum = two_letter * three_letter
print("The checksum for the list of box IDs is:", checksum)


### Puzzle part 2 ###
# form a list of entries
box = []

path2 = 'Day2.txt'
try:
    with open(path2, newline='\n') as f2:
        for line in f2:
            line = line.replace('\n', '')
            box.append(line)
except FileNotFoundError:
    f = ""

# print(box) # debug chk for import of lines
# print(len(box))

# What are the number of differences between strings      
def string_diff(s1, s2):
    return sum(1 if c1 != c2 else 0 for c1, c2 in zip(s1, s2))

# What are the common letters
def common_letters(s1, s2):
    return ''.join(c1 if c1 == c2 else '' for c1, c2 in zip(s1, s2))

# Find the common letters by first identifying the only strings with one diff
for i in range(len(box)):
    for j in range(i + 1, len(box)):
        if string_diff(box[i], box[j]) == 1:
            print(common_letters(box[i], box[j]))
