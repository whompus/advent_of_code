#!/usr/bin/env python3

#!/usr/bin/env python3

lines = open("wtfinput.txt").read().splitlines()

elves = []

calorie_count = 0

for line in lines:
    if line != "":
        calorie_count += int(line)
    elif line == "":
        elves.append(int(calorie_count))
        calorie_count = 0
    else:
        elves.append(int(calorie_count))

elves.sort()

top_three_result = sum(elves[-3:])

print(top_three_result)
