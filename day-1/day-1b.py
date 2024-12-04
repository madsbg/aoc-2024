numbers_left = []
numbers_right = []

with open('puzzle-input.txt', 'r') as file:
    for line in file:
        number_pairs = line.split()
        numbers_left.append(number_pairs[0])
        numbers_right.append(number_pairs[1])
total_similarity = 0
for left_number in numbers_left:
    occurrences = 0
    similarity_score = 0
    for right_number in numbers_right:
        if right_number == left_number:
            occurrences += 1
    similarity_score = int(left_number) * occurrences
    print(left_number, occurrences, similarity_score)
    total_similarity += similarity_score
print(total_similarity)
