"""Day 6 Advent of Code"""

with open("input.txt") as file:
    datastream = file.read()

def find_marker(datastream:str, extra: int ):
    for idx, __ in enumerate(datastream, 1):
        if len(datastream) - idx - extra > 0:
            if len(datastream[idx:idx+extra]) == len(set(datastream[idx:idx+extra])):
                break
    return idx + extra


index_marker = find_marker(datastream, extra=14) 
print(f"first marker at index {index_marker}")