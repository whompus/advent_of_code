#!/usr/bin/env python3

lines = open("simple_input.txt").read().splitlines()

elves = []
calorie_count = 0

for line in lines:
    if line != "":
        calorie_count += int(line)
    else:
        elves.append(int(calorie_count))
        calorie_count = 0

elves.append(int(calorie_count))

elves.sort()

print(elves)

top_three = elves[-3:]

top_three_result = 0

for i in top_three:
    top_three_result += i

print(top_three_result)
