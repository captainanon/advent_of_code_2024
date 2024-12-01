import functools

input = 'day_1/input.txt'

def solve(input):
    with open(input) as file:
        lst_1 = []
        lst_2 = []
        for line in file.readlines():
            lst_1.append(int(line.strip().split('   ')[0]))
            lst_2.append(int(line.strip().split('   ')[1]))
    lst_1.sort()
    lst_2.sort()
    lst = list(zip(lst_1, lst_2))   
    return sum(map(lambda x: abs(x[0]-x[1]), lst))

if __name__ == '__main__':
    print(solve(input)) # 2166959