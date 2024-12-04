numbers_left = []
numbers_right = []

with open('puzzle-input.txt', 'r') as file:
    for line in file:
        number_pairs = line.split()
        numbers_left.append(number_pairs[0])
        numbers_right.append(number_pairs[1])
numbers_left.sort()
numbers_right.sort()
total_distance = 0
for number_pair in range(len(numbers_left)):
    print(numbers_left[number_pair], numbers_right[number_pair])
    number_distance = abs(int(numbers_left[number_pair]) - int(numbers_right[number_pair]))
    print(number_distance)
    total_distance += number_distance
print(total_distance)
