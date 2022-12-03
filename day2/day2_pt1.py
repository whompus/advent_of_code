#!/usr/bin/env python3

# my_rock = "X"
# my_paper = "Y"
# my_scissor = "Z"

# op_rock = "A"
# op_paper = "B"
# op_scissor = "C"

# lost_score = 0
# draw_score = 3
# win_score = 6

# rock_score = 0
# paper_score = 2
# scissor_score = 3

# define when i win
my_wins = {"A": "Y", "B": "Z", "C": "X"}

# define when i draw
my_draws = {"A": "X", "B": "Y", "C": "Z"}

# define what is tool is worth
scores = {"X": 1, "Y": 2, "Z": 3}

total_score = 0
round_score = 0

lines = open("input.txt")
for line in lines:
    key, value = line.split()
    # win
    if (key, value) in my_wins.items():
        round_score += scores[value]
        round_score += 6
    # draw
    elif (key, value) in my_draws.items():
        round_score += scores[value]
        round_score += 3
    # loss
    else:
        round_score += scores[value]
    total_score += round_score
    round_score = 0
print("Total score:", total_score)
