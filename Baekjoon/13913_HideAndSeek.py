import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/BFS'))
from HideAndSeek import HideSeek

import sys
def main():
  input = sys.stdin.readline
  start, end = list(map(int, input().split()))
  walk = 1
  fly = 2

  hs = HideSeek(start, end, walk, fly)
  route = hs.route()
  count = len(route[0]) - 1
  print(count)
  print(' '.join(map(str, route[0])))


main()
