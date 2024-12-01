from collections import Counter

input = 'day_1/input.txt'

def solve(input):
    with open(input) as file:
        lst_1 = []
        lst_2 = []
        for line in file.readlines():
            lst_1.append(int(line.strip().split('   ')[0]))
            lst_2.append(int(line.strip().split('   ')[1]))
    counter = Counter(lst_2)
    sum_ = 0
    for num in lst_1:
        sum_ += num * counter[num]
    return sum_

if __name__ == '__main__':
    print(solve(input)) # 23741109