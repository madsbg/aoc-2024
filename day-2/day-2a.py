
with open('puzzle-input.txt', 'r') as puzzle_input:
    safe_reports = 0
    for report in puzzle_input:
        levels = report.split()
        # print(levels)
        # for level in range(1, len(levels)):
        #     print(int(levels[level-1]) - int(levels[level]))
        levels_diffs = [int(levels[level]) - int(levels[level-1]) for level in range(1, len(levels))]
        print(levels_diffs)
        pass
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
            safe_reports += 1
    print(safe_reports)
