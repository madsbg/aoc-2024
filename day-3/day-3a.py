import re

with open('puzzle-input.txt', 'r') as puzzle_input:
    total_sum = 0
    for corrupted_memory in puzzle_input:
        instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", corrupted_memory)
        for instruction in instructions:
            total_sum += int(instruction[0]) * int(instruction[1])
    print(total_sum)
