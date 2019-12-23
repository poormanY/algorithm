import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/BFS'))
from Maze import MazeBFS

import sys
def main():
  height, width = list(map(int, sys.stdin.readline().split()))
  d = MazeBFS(width,height)
  for y, line in enumerate(sys.stdin):
    for x, value in enumerate(line):
      if value == '1':
        d.add_route(x,y)
  cnt = d.search()
  print(cnt)

main()
