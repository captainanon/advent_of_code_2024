from collections import defaultdict

input = 'day_5/input.txt'

def solve(input):
    with open(input) as file:
        input = file.read().split('\n\n')
        rules = defaultdict(list)
        for line in input[0].split():
            line = line.split('|')
            rules[line[0]].append(line[1])
        middle_nums = []
        for line in input[1].split():
            pages = line.split(',')
            passed_test = True
            for idx, num in enumerate(pages):
                for page in pages[:idx]:
                    if page in rules[num]:
                        passed_test = False
                        break
                if not passed_test:
                    break
            if passed_test:
                middle_nums.append(pages[len(pages)//2]) 
    return sum(map(int, middle_nums))   

if __name__ == '__main__':
    print(solve(input)) # 4814