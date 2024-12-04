import re
from functools import reduce

input = 'day_3/input.txt'

def solve(input):
    with open(input) as file:
        memory = file.read()
    idx = memory.find('don\'t()')
    sum_ = 0
    while memory:
        if idx != -1:
            temp_memory = memory[:idx]
        else:
            temp_memory = memory
        pattern = 'mul\(\d+,\d+\)'
        matches = re.findall(pattern, temp_memory)
        pattern = '\d+'
        nums = [list(map(int, y)) for y in (re.findall(pattern, x) for x in matches)]
        sum_ += sum(map(lambda z: reduce(lambda x,y: x*y, z), nums))
        if idx != -1:
            memory = memory[idx+7:]
        else:
            break
        idx = memory.find('do()')
        if idx != -1:
            memory = memory[idx+4:]
        else:
            break
        idx = memory.find('don\'t()')
    return sum_

if __name__ == '__main__':
    print(solve(input)) # 87163705