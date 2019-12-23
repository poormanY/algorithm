import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# DFS : Depth First Search
# BFS : Breadth First Search
from collections import defaultdict
from collections import deque

class GraphBFS():
  def __init__(self):
    self.graph = defaultdict(list)
    self.node = []

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def sortEdge(self):
    for i in self.graph:
      self.graph[i] = list(sorted(self.graph[i]))

  def BFS(self, s, search=None):
    self.node = []
    self.count = 0
    visited = defaultdict(lambda: False)
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
      s = queue.popleft()
      self.node.append(s)
      for i in self.graph[s]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True
    return self.node

# Main Function
def main():
  bfs = GraphBFS()

  datas = [(1,2),(2,3),(2,4),(3,4),(3,5),(4,2),(5,3),(5,6)]
  for x, y in datas:
    bfs.addEdge(x,y)

  start = 3
  bfs_node = bfs.BFS(start)

  print(' '.join(list(map(str, bfs_node))))

if __name__ == '__main__':
  main()
