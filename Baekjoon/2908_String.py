import sys
input = sys.stdin.readline

words = input().split()
A, B = map(int, map(lambda x: x[::-1], words))
print(max(A,B))
