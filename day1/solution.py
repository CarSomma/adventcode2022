"""Day 1 Advent of Code: 
My objective:
Use/Explore:
    1. python built-function
    2. list methods
    3. string methods
"""
with open("input.txt") as file:
    input_ = file.read().splitlines()

# part 1 
sums_list = list()
sum_ = 0
for num in input_:
    if num.isnumeric():
        sum_ = sum_ + int(num)
    else:
        sums_list.append(sum_)
        sum_ = 0


max_calories = max(sums_list)
which_elf = sums_list.index(max_calories) + 1
print(f"The elf {which_elf}th has cumulated {max_calories} calories")
    
# part2 find out the top3-elf total ammount calories 

sums_list.sort(reverse=True)
top3_elf_total_ammount_calories = sum(sums_list[:3])
print(f"the top3-elf total calories ammount  is {top3_elf_total_ammount_calories}")