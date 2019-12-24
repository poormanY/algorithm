import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from collections import deque
from collections import defaultdict
from copy import copy
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
        if y == self.end:
          return visited[y] - 1
        queue.append(y)

  def route(self):
    visited = defaultdict(list)
    cur_queue = deque()
    next_queue = deque([self.start])
    while(queue):
      x = queue.popleft()


  def route2(self):
    cur_visited = defaultdict(int)
    next_visited = defaultdict(int)
    next_visited[self.start] = 1
    cur_queue = deque()
    next_queue = deque([[self.start]])
    route_end = False
    while(next_queue):
      cur_queue, next_queue = next_queue, deque()
      cur_visited = copy(next_visited)  # deep copy
      while(cur_queue):
        q = cur_queue.popleft()
        x = q[-1]
        yy = [x-self.walk, x+self.walk, x*self.fly]
        if x > self.end:
          yy = [x-self.walk]
        for y in yy:
          if y < 0:
            continue
          if cur_visited[y] > 0:
            continue
          next_q = q + [y]
          next_queue.append(next_q)
          next_visited[y] = next_visited[x] + 1
          if y == self.end:
            route_end = True
            yield next_q
      if route_end == True:
        break

def main():
  start, end = 5, 17
  start, end = 3, 150
  walk = 1
  fly = 2

  hs = HideSeek(start, end, walk, fly)
  count = hs.count()
  print(count)
  route = list(hs.route())
  print(route)
  count = len(route[0])-1
  routeCnt = len(route)
  print(count)
  print(routeCnt)

if __name__ == '__main__':
  main()
