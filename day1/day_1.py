#!/usr/bin/env python3

with open("simple_input.txt", "r") as file:

    calories_exist = True
    elves = []
    calorie_count = 0

    for line in file:
        if line != "\n":
            calorie_count += int(line)
        else:
            elves.append(int(calorie_count))
            calorie_count = 0

elves.append(int(calorie_count))

elves.sort()

print(elves)

print("Largest:", elves[-1])
