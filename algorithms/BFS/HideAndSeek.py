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

  def graph2lst(self, graph, start, end):
    queue = deque([[end]])
    while(queue):
      if queue[0][0] == start:
        break
      lst = queue.popleft()
      x = lst[0]
      for y in graph[x]:
        queue.append([y] + lst)
    return queue

  def route(self):
    visited = defaultdict(int)
    visited[self.start] = 1
    graph = defaultdict(set)

    queue = deque([self.start])
    max_count = self.start // self.walk + 1
    while(queue):
      x = queue.popleft()
      if visited[x] > max_count:
        break
      yy = [x-self.walk, x+self.walk, x*self.fly]
      if x > self.end:
        yy = [x-self.walk]
      for y in yy:
        if y < 0:
          continue
        if (visited[y] > 0) and (visited[y] <= visited[x]):
          continue
        visited[y] = visited[x] + 1
        graph[y].add(x)
        queue.append(y)
        if y == self.end:
          max_count = visited[y]
    lst = self.graph2lst(graph, self.start, self.end)
    return lst

def main():
  start, end = 5, 17
  start, end = 5, 15
  walk = 1
  fly = 2

  hs = HideSeek(start, end, walk, fly)
  count = hs.count()
  print(count)
  route = hs.route()
  print(route)
  count = len(route[0])-1
  routeCnt = len(route)
  print(count)
  print(routeCnt)
  for r in route:
    print(' '.join(map(str, r)))

if __name__ == '__main__':
  main()
