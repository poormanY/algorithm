import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/DP'))
from CountSum import DP

import sys
def main():
  input = sys.stdin.readline
  T = int(input())
  args = [1,2,3]
  for line in sys.stdin:
    n = int(line)
    d = DP()
    count = d.count(n, args)
    print(count)

main()
