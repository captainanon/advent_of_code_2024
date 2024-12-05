input = 'day_4/input.txt'

def solve(input):
    with open(input) as file:
        puzzle = [list(x.strip()) for x in file.readlines()]
    r_ = len(puzzle)
    c_ = len(puzzle[0])
    count = 0
    for r in range(r_):
        for c in range(c_):
            # check right
            temp = ''
            for i in range(4):
                if c+i < c_:
                    temp += puzzle[r][c+i]
                else:
                    break
            if temp == 'XMAS':
                count += 1
            # check right-down diag
            temp = ''
            for i in range(4):
                if r+i < r_ and c+i < c_:
                    temp += puzzle[r+i][c+i]
                else:
                    break
            if temp == 'XMAS':
                count += 1
            # check down
            temp = ''
            for i in range(4):
                if r+i < r_:
                    temp += puzzle[r+i][c]
                else:
                    break
            if temp == 'XMAS':
                count += 1
            # check left-down diag
            temp = ''
            for i in range(4):
                if r+i < r_ and c-i >= 0:
                    temp += puzzle[r+i][c-i]
                else:
                    break
            if temp == 'XMAS':
                count += 1
            # check left
            temp = ''
            for i in range(4):
                if c-i >= 0:
                    temp += puzzle[r][c-i]
                else:
                    break
            if temp == 'XMAS':
                count += 1
            # check left-up diag
            temp = ''
            for i in range(4):
                if r-i >= 0 and c-i >= 0:
                    temp += puzzle[r-i][c-i]
                else:
                    break
            if temp == 'XMAS':
                count += 1
            # check up
            temp = ''
            for i in range(4):
                if r-i >= 0:
                    temp += puzzle[r-i][c]
                else:
                    break
            if temp == 'XMAS':
                count += 1
            # check up-right diag
            temp = ''
            for i in range(4):
                if r-i >= 0 and c+i < c_:
                    temp += puzzle[r-i][c+i]
                else:
                    break
            if temp == 'XMAS':
                count += 1
    return count

if __name__ == '__main__':
    print(solve(input)) # 2297