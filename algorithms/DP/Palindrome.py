import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class DP():
  def __init__(self):
    self.isPalidrome = []
    self.max_n = 0

  def palidrome(self, S):
    n = len(S)
    self.isPalidrome = [[0 for i in range(n)] for j in range(n)]
    # len 1
    for i in range(n):
      self.isPalidrome[i][i] = 1
      self.max_n = 1
    # len 2
    for i in range(n-1):
      j = i + 1
      if S[i] == S[j]:
        self.isPalidrome[i][j] = 1
        self.max_n = 2
    # len >= 3
    for d in range(2, n):
      for i in range(n-d):
        j = i + d
        if S[i] == S[j] and self.isPalidrome[i+1][j-1] == 1:
          self.isPalidrome[i][j] = 1
          self.max_n = d + 1

  def isValid(self, s, e):
    return self.isPalidrome[s-1][e-1]

  def max(self):
    return self.max_n

def main():
  S = '1213121'

  d = DP()
  d.palidrome(S)
  for i in range(1,len(S)+1):
    for j in range(1,len(S)+1):
      if d.isValid(i,j) == 1:
        print(i,j,S[i-1:j])

if __name__ == '__main__':
  main()
