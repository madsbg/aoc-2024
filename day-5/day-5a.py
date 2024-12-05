page_pairs = {}
page_updates = []


def main():
    read_puzzle_input()
    check_page_updates()


def read_puzzle_input():
    with open('puzzle-input.txt', 'r') as puzzle_input:
        for line in puzzle_input:
            if "|" in line:
                page_pair = line.strip().split("|")
                if page_pair[0] not in page_pairs:
                    page_pairs[page_pair[0]] = []
                page_pairs[page_pair[0]].append(page_pair[1])
            elif "," in line:
                page_updates.append(line.strip().split(","))


def check_page_updates():
    total_sum = 0
    for page_update in page_updates:
        middle_number = correct_order(page_update)
        if middle_number:
            total_sum += int(middle_number)
    print(total_sum)


def correct_order(page_update):
    print()
    print(page_update)
    for page_index in range(len(page_update)-1, 0, -1):
        print(page_update[page_index], page_pairs[page_update[page_index]])
        for page in page_pairs[page_update[page_index]]:
            if page in page_update[:page_index]:
                print("Error:", page)
                return False
    return page_update[int((len(page_update) - 1) / 2)]


if __name__ == "__main__":
    main()
