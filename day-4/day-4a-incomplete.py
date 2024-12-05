with (open('puzzle-input.txt', 'r') as puzzle_input):
    xmas_grid = []
    row_index = 0
    for row in puzzle_input:
        row_index += 1
        # print(row_index, row)
        column_index = 0
        columns = []
        for column in row.strip():
            columns.append(column)
            column_index += 1
            # print(column_index, column)
        xmas_grid.append(columns)
        # print(row_index, columns)
    for grid_row in xmas_grid:
        for grid_row_index in range(len(xmas_grid)):
            for grid_column_index in range(len(grid_row)):
                # print(f"{xmas_grid[grid_row_index][grid_column_index]}[{grid_row_index},{grid_column_index}] ", end="")
                if (xmas_grid[grid_row_index][grid_column_index] == "S"
                    and xmas_grid[grid_row_index][grid_column_index - 1] == "A"
                    and xmas_grid[grid_row_index][grid_column_index - 2] == "M"
                    and xmas_grid[grid_row_index][grid_column_index - 3] == "X"):
                    print(f"AS[{grid_row_index},{grid_column_index}] " , end="")
            print()
