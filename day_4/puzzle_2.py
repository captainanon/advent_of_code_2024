input = 'day_4/input.txt'

def solve(input):
    with open(input) as file:
        puzzle = [list(x.strip()) for x in file.readlines()]
    r_ = len(puzzle)
    c_ = len(puzzle[0])
    count = 0
    for r in range(r_):
        for c in range(c_):
            if (
                    puzzle[r][c] == 'A' and
                    (
                        (
                            r-1 >= 0 and c+1 < c_ and puzzle[r-1][c+1] == 'M' and r+1 < r_ and c-1 >= 0 and puzzle[r+1][c-1] == 'S'
                        ) or
                        (
                            r-1 >= 0 and c+1 < c_ and puzzle[r-1][c+1] == 'S' and r+1 < r_ and c-1 >= 0 and puzzle[r+1][c-1] == 'M'
                        )
                    ) and
                    (
                        (
                            r-1 >= 0 and c-1 >= 0 and puzzle[r-1][c-1] == 'M' and r+1 < r_ and c+1 < c_ and puzzle[r+1][c+1] == 'S'
                        ) or
                        (
                            r-1 >= 0 and c-1 >= 0 and puzzle[r-1][c-1] == 'S' and r+1 < r_ and c+1 < c_ and puzzle[r+1][c+1] == 'M'
                        )
                    )
                ):
                count += 1
    return count

if __name__ == '__main__':
    print(solve(input)) # 1745