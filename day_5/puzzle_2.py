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
            add_ = False
            for idx, num in enumerate(pages):
                for page in pages[:idx]:
                    if page in rules[num]:
                        passed_test = False
                        break
                if not passed_test:
                    break
            while not passed_test:
                passed_test = True
                add_ = True
                new_list = []
                for idx, num in enumerate(pages):
                    new_list.append(num)
                    for page in pages[:idx]:
                        if page in rules[num]:
                            new_list.remove(page) if page in new_list else new_list
                            new_list.append(page)
                            passed_test = False
                pages = [x for x in pages if x not in new_list] 
                new_list.extend(pages)
                pages = new_list
            if add_:
                middle_nums.append(pages[len(pages)//2]) 
    return sum(map(int, middle_nums))   

if __name__ == '__main__':
    print(solve(input)) # 5448