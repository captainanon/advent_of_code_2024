input = 'day_2/input.txt'

def solve(input):
    with open(input) as file:
        count = 0
        for line in file.readlines():
            report = list(map(int, line.strip().split()))
            temp_count = 0
            for idx in range(len(report)):
                temp_report = [x for i,x in enumerate(report) if i!=idx]
                temp = [i-j for i,j in zip(temp_report[:-1],temp_report[1:])]
                is_increasing = all(map(lambda x: (x>=1 and x<=3) if x>0 else False, temp))
                is_decreasing = all(map(lambda x: (x>=-3 and x<=-1) if x<0 else False, temp))
                temp_count += 1 if is_increasing or is_decreasing else 0
            count += 1 if temp_count >= 1 else 0
    return count

if __name__ == '__main__':
    print(solve(input)) # 544