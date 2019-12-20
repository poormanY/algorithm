import sys
input = sys.stdin.readline
from collections import defaultdict

class Prime:
  def __init__(self):
    self.primes = defaultdict(lambda: True)

  def prime_list(self, n, start=2):
    start = max(2, start)
    m = int(n ** 0.5)
    for i in range(2, m+1):
      if self.primes[i] == True:
        for j in range(i+i, n+1, i):
          self.primes[j] = False
    return [i for i in range(start,n+1) if self.primes[i] == True]

def main():
  M, N = list(map(int,input().split()))
  p = Prime()
  for x in p.prime_list(N, M):
    print(x)

main()
