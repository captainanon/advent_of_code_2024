import re
from functools import reduce

input = 'day_3/input.txt'

def solve(input):
    with open(input) as file:
        memory = file.read()
    pattern = 'mul\(\d+,\d+\)'
    matches = re.findall(pattern, memory)
    pattern = '\d+'
    nums = [list(map(int, y)) for y in (re.findall(pattern, x) for x in matches)]
    return sum(map(lambda z: reduce(lambda x,y: x*y, z), nums))

if __name__ == '__main__':
    print(solve(input)) # 178886550