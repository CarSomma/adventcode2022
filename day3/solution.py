"""Day 3 Advent of Code: 
My objective:
Use/Explore:
    1. python built-function
    2. list methods
    3. string methods
    4. string package
    5. nested if statements
"""

import string
with open("input.txt") as file:
    rucksacks = file.read().splitlines()

a_to_z = string.ascii_lowercase
A_to_Z = a_to_z.upper()

# Part 1
def split_string(string_:str) -> tuple:
    first_half = string_[:len(string_)//2]
    second_half = string_[len(string_)//2:]
    return (first_half, second_half)

sum_priorities = 0
for rucksack in rucksacks:
    first_compart, second_compart = split_string(rucksack)
    for char in first_compart:
        #print(char)
        if char in second_compart:
            if char in a_to_z:
                priorities = list(a_to_z).index(char) + 1 
                sum_priorities += priorities
                break
            else:
                priorities = 26 + list(A_to_Z).index(char) +1 
                sum_priorities += priorities
                break

print(f"The sum of priorities is {sum_priorities}")

# Part 2 
def get_3_elfs_group(rucksacks:list):

    return [
        rucksacks[index:index+3] \
            for index, __ in enumerate(rucksacks) if index % 3 == 0
        ]

sum_priorities = 0
for groups in get_3_elfs_group(rucksacks):
    group1, group2, group3 = groups
    for char in group1:
        if char in group2 and char in group3:
            if char in a_to_z:
                priorities = list(a_to_z).index(char) + 1 
                sum_priorities += priorities
                break
            else:
                priorities = 26 + list(A_to_Z).index(char) +1 
                sum_priorities += priorities
                break
            

print(f"The sum of priorities is {sum_priorities}")


