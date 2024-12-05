import re

with open('puzzle-input.txt', 'r') as puzzle_input:
    total_sum = 0
    corrupted_memory = puzzle_input.read().replace("\r\n", "").replace("\n", "")
    valid_data = re.sub(r"don't\(\).+?(do\(\)|$)", "", corrupted_memory)
    instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", valid_data)
    for instruction in instructions:
        total_sum += int(instruction[0]) * int(instruction[1])
    print(total_sum)
