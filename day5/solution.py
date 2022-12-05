"""Day 5 Advent of Code: 
My objective:
Use/Explore:
    1. python built-functions (open, zip, enumerate)
    2. list methods (extend, append)
    3. string methods (isalpha, isnumeric, readlines, join)
    4. dictionary methods (keys, values)
        dictionary comprehension
    5. re library 
"""

import re

def move_crates(
    n_items:int, from_crate:int, 
    to_crate:int, crates:dict 
    ):
    
    to_extend = crates[from_crate][-n_items:]
    
    #to_extend.reverse() commented for part 2
    
    crates[from_crate] = crates[from_crate][:-n_items]
    crates[to_crate].extend(to_extend)
    return crates

with open("input.txt") as file:
    lines = file.readlines()
    crates = lines[:lines.index("\n")]
    instructions = lines[lines.index("\n")+1 : ]


crates.reverse()


dict_crates = dict()
crater_num_list = list()
for crate in crates:
    for column, char in enumerate(crate):
        if char.isnumeric():
            crater_num_list.append(int(char))
        elif char.isalpha():
            if column not in dict_crates.keys():
                dict_crates[column] = []
                dict_crates[column] += [char]
            else:
                dict_crates[column] += [char]
   
dict_crates = {key:value for key, value in zip(crater_num_list,dict_crates.values())}

last_crates = dict_crates.copy()

values_list = list()
for line_nr, instruction_line in enumerate(instructions,1):
    #print(instruction_line)
    n_items, from_crate, to_crate =re.findall("\d+",instruction_line)
    last_crates = move_crates(int(n_items),int(from_crate),int(to_crate),last_crates)
    if line_nr == len(instructions):
        for value_list in last_crates.values():
            values_list.append(value_list[-1])

message_to_elf = "".join(values_list)
print(f"Hi Elfs here the message {message_to_elf}")
