#!/usr/bin/env python3

lines = open("wtfinput.txt").read().splitlines()

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

print("Largest:", elves[-1])
