import sys
input = sys.stdin.readline
n = int(input())
for line in sys.stdin:
    total = 0
    score = 0
    for s in line.rstrip():
        if s == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
