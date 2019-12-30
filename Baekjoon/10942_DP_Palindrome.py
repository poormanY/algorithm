import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/DP'))
from Palindrome import DP

import sys
def main():
  input = sys.stdin.readline
  n = int(input())
  S = []
  for x in input().split():
    S.append(x)
  T = int(input())

  d = DP()
  d.palidrome(S)
  for i in range(T):
    s,e = map(int, input().rstrip().split())
    v = d.isValid(s,e)
    print(v)

main()
