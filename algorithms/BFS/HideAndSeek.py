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
    visited = defaultdict(int)
    queue = deque([self.start])
    visited[self.start] = 1
    while(queue):
      x = queue.popleft()
      if x == self.end:
        return visited[x] - 1
      yy = [x-self.walk, x+self.walk, x*self.fly]
      if x > self.end:
        yy = [x-self.walk]
      for y in yy:
        if y < 0:
          continue
        if visited[y] > 0:
          continue
        visited[y] = visited[x] + 1
        queue.append(y)

def main():
  start, end = 5, 17
  start, end = 10, 0
  walk = 1
  fly = 2

  hs = HideSeek(start, end, walk, fly)
  count = hs.count()
  print(count)

if __name__ == '__main__':
  main()
