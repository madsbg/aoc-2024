def main():
    read_puzzle_input()


def read_puzzle_input():
    with open('puzzle-input.txt', 'r') as puzzle_input:
        safe_reports = 0
        for report in puzzle_input:
            levels = report.split()
            print()
            if safe_level(levels):
                safe_reports += 1
                continue
            else:
                if safe_sub_level(levels):
                    safe_reports += 1
                    print(safe_reports)
            pass
        print(safe_reports)


def safe_sub_level(levels):
    for position in range(len(levels)):
        sub_level = levels.pop(position)
        print(position, sub_level, end=" ")
        if safe_level(levels):
            return True
        levels.insert(position, sub_level)
    return False


def safe_level(levels):
    levels_diffs = [int(levels[level]) - int(levels[level - 1]) for level in range(1, len(levels))]
    print(f"{levels} {levels_diffs}", end="")
    ascending = 0
    descending = 0
    unsafe = 0
    for diff in levels_diffs:
        if -3 <= diff <= -1:
            descending += 1
        elif 1 <= diff <= 3:
            ascending += 1
        else:
            unsafe += 1
    if (ascending == 0 or descending == 0) and unsafe == 0:
        print(" - Safe")
        return True
    else:
        print(" - Unsafe")
        return False


if __name__ == "__main__":
    main()
