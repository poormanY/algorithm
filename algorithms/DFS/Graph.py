import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# DFS : Depth First Search
# BFS : Breadth First Search
from collections import defaultdict

class GraphDFS():
  def __init__(self):
    self.graph = defaultdict(list)
    self.node = []

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def sortEdge(self):
    for i in self.graph:
      self.graph[i] = list(sorted(self.graph[i]))

  def DFSUtil(self, v, visited):
    visited[v] = True
    self.node.append(v)
    for i in self.graph[v]:
      if visited[i] == False:
        self.DFSUtil(i, visited)

  def DFS(self, s):
    self.node = []
    visited = defaultdict(lambda: False)
    self.DFSUtil(s, visited)
    return self.node

# Main Function
def main():
  dfs = GraphDFS()

  datas = [(1,2),(2,3),(2,4),(3,4),(3,5),(4,2),(5,3),(5,6)]
  for x, y in datas:
    dfs.addEdge(x,y)

  start = 3
  dfs_node = dfs.DFS(start)

  print(' '.join(list(map(str, dfs_node))))

if __name__ == '__main__':
  main()
