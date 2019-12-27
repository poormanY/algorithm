import sys
from collections import deque
def main():
  input = sys.stdin.readline
  start, end = list(map(int, input().split()))

  #start, end = 5, 17
  #start, end = 5, 15
  #start, end = 5, 1
  #start, end = 3,10
  walk = 1
  fly = 2

  max_val = max(start+1, end*fly)
  max_visit = abs(end-start)+1
  visited = [0] * (max_val)
  ways = [0] * (max_val)
  visited[start] = 1
  ways[start] = 1

  queue = deque([start])
  while(queue):
    x = queue.popleft()
    if visited[x] >= max_visit:
      continue
    y = x*fly
    while(0 < y < max_val):
      if 0 < visited[y] <= visited[x]:
        y = y*fly
        continue
      if visited[y] == 0:
        visited[y] = visited[x]
        queue.append(y)
      ways[y] = ways[x]
      y = y*fly

    for y in [x-walk,x+walk]:
      if y < 0 or y >= max_val:
        continue
      if 0 < visited[y] <= visited[x]:
        continue
      if visited[y] == 0:
        visited[y] = visited[x] + 1
        queue.append(y)
      ways[y] += ways[x]
      if y == end:
        max_visit = visited[y]
  count_visit = visited[end]-1
  count_ways = ways[end]
  print(count_visit)
  #print(count_ways)
  
main()
