"""Day 4 Advent of Code: 
My objective:
Use/Explore:
    1. python built-functions
    2. list methods
    3. string methods
    4. set methods
"""
with open("input.txt") as file:
    pairs = file.read().splitlines()

def get_set_range(str_range:str) -> set[int]:
    both_nums = str_range.split("-")
    start_num = int(both_nums[0])
    stop_num = int(both_nums[1])
    return set(range(start_num, stop_num +1))

count_fully_contained = 0
for __, pair in enumerate(pairs):
    first_range_str, second_range_str = pair.split(",")
    first_set = get_set_range(first_range_str)
    second_set = get_set_range(second_range_str)
    if first_set.issubset(second_set) or second_set.issubset(first_set):
        count_fully_contained += 1
    # Part 2
    elif not first_set.isdisjoint(second_set): 
         count_fully_contained += 1
    


print(f"The pairs with duplicates are {count_fully_contained}")

    
