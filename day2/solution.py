"""Day 2 Advent of Code: 
My objective:
Use/Explore:
    1. python built-function
    2. list methods
    3. string methods
    4. nested dictionary
"""

with open("input.txt") as file:
    matches = file.readlines()

def get_base_score(plays:list, play:str) -> int:
    return plays.index(play) + 1 

# Part 1
# R=Rock, P=Paper, S=Scissors 
PLAYS = ["R", "P", "S"]

OPPONENT_GAME = dict(A="R", B="P", C="S")
ME_GAME = dict(X="R", Y="P", Z="S")
my_total_score = 0
for match in matches:
    opponent, me = match.split()
    if OPPONENT_GAME[opponent] == ME_GAME[me]:
        my_total_score += get_base_score(PLAYS, ME_GAME[me]) + 3
    else:
        if OPPONENT_GAME[opponent] == "R" and ME_GAME[me] == "P":
            my_total_score += get_base_score(PLAYS, ME_GAME[me]) + 6
        elif OPPONENT_GAME[opponent] == "P" and ME_GAME[me] == "S":
            my_total_score += get_base_score(PLAYS, ME_GAME[me]) + 6
        elif OPPONENT_GAME[opponent] == "S" and ME_GAME[me] == "R":
            my_total_score += get_base_score(PLAYS, ME_GAME[me]) + 6
        else:
            my_total_score += get_base_score(PLAYS, ME_GAME[me]) + 0

print(f"My total score at ROCK, PAPER and SCISSORS is {my_total_score}")

# Part 2
# X means you lose, Y it is a draw, Z you win


ME_GAME_part2 = {
    "X":{
        "R":"S",
        "P":"R",
        "S":"P"
    },
    "Z":{
        "R":"P",
        "P":"S",
        "S":"R"
    }
}

my_total_score_part2 = 0
for match in matches:
    opponent, me = match.split()
    if me == "Y":
        my_total_score_part2 += get_base_score(PLAYS, OPPONENT_GAME[opponent]) + 3
    elif me == "Z":
        opponent_play = OPPONENT_GAME[opponent]
        my_play = ME_GAME_part2[me][opponent_play]
        my_total_score_part2 +=get_base_score(PLAYS, my_play) + 6
    else:
        opponent_play = OPPONENT_GAME[opponent]
        my_play = ME_GAME_part2[me][opponent_play]
        my_total_score_part2 +=get_base_score(PLAYS, my_play) + 0
        

print(f"My total score at ROCK, PAPER and SCISSORS with elf instructions is  {my_total_score_part2}")