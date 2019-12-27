import sys
T = int(sys.stdin.readline())
for line in sys.stdin:
    R, S = line.split()
    P = ''
    for s in S:
        for i in range(int(R)):
            P += s
    print(P)
