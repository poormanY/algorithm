import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/BFS'))
from HideAndSeek import HideSeek


def main():
  start, end = 5, 17
  walk = 1
  fly = 2

  hs = HideSeek(start, end, walk, fly)
  count = hs.count()
  print(count)

if __name__ == '__main__':
  main()
