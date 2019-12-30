import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
예제 출력 1
1
0
1
1
'''

class DP():
  def __init__(self):
    self.isPalidrome = []

  def palidrome(self, S):
    n = len(S)
    self.isPalidrome = [[0]*n for i in range(n)]
    for i in range(n):
      self.isPalidrome[i][i] = 1
    for i in range(n-1):
      if S[i] == S[i+1]:
        self.isPalidrome[i][i+1] = 1
    for d in range(2,n):
      for i in range(n-d):
        j = i + d
        if S[i] != S[j]:
          continue
        if self.isPalidrome[i+1][j-1] == 0:
          continue
        self.isPalidrome[i][j] = 1

  def isValid(self, s, e):
    return self.isPalidrome[s-1][e-1]

import sys
def main():
  input = sys.stdin.readline
  n = int(input())
  S = ''.join(input().split())
  T = int(input())

  d = DP()
  d.palidrome(S)
  for line in sys.stdin:
    s,e = map(int, line.split())
    v = d.isValid(s,e)
    print(v)

if __name__ == '__main__':
  main()
