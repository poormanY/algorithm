import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from collections import deque
from collections import defaultdict
class HideSeek():
  def __init__(self, start, end, walk=1, fly=2):
    self.start = start
    self.end = end
    self.walk = walk
    self.fly = fly

  def count(self):
    if self.start == self.end:
      return 0
    visited = defaultdict(lambda: False)

    cur_queue = deque()
    next_queue = deque([self.start])
    visited[self.start] = True
    cnt = 0
    while(next_queue):
      cur_queue = next_queue
      next_queue = deque()
      cnt += 1
      while(cur_queue):
        x = cur_queue.popleft()
        for y in [x-self.walk,x+self.walk,x*self.fly]:
          if (y < 1) or (y > self.end + 1):
            continue
          if visited[y] == False:
            visited[y] = True
            next_queue.append(y)
            if y == self.end:
              return cnt


def main():
  start, end = 5, 17
  start, end = 5, 14
  walk = 1
  fly = 2

  hs = HideSeek(start, end, walk, fly)
  count = hs.count()
  print(count)

if __name__ == '__main__':
  main()
