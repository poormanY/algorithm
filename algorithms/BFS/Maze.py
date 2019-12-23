import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from collections import deque
class MazeBFS():
  def __init__(self, width, height):
    self.route = [[-1]*width for i in range(height)]
    self.width = width
    self.height = height

  def add_route(self, x, y):
    self.route[y][x] = 0

  def print_route(self):
    for line in self.route:
      print(line)

  def is_route(self, x, y):
    if x < 0 or x >= self.width:
      return False
    if y < 0 or y >= self.height:
      return False
    if self.route[y][x] == -1:
      return False
    if self.route[y][x] > 0:
      return False
    return True

  def search(self, start=None, end=None):
    if not start: start = [0,0]
    if not end:   end = [self.width-1, self.height-1]
    s_x, s_y = start
    e_x, e_y = end

    cur_queue = deque()
    next_queue = deque([[s_x, s_y]])
    count = 1
    self.route[s_y][s_x] = count
    while(next_queue):
      cur_queue = next_queue
      next_queue = deque()
      count += 1
      while(cur_queue):
        x, y = cur_queue.popleft()
        for _x, _y in [[1,0],[-1,0],[0,1],[0,-1]]:
          if self.is_route(x+_x, y+_y):
            next_queue.append([x+_x,y+_y])
            self.route[y+_y][x+_x] = count
            if end == [x+_x, y+_y]:
              return count

def main():
  width, height = 6, 4
  lines = ['101111','101010','101011','111011']

  d = MazeBFS(width,height)
  for y, line in enumerate(lines):
    for x, value in enumerate(line):
      if value == '1':
        d.add_route(x,y)

  d.print_route()
  cnt = d.search()
  print(cnt)
  d.print_route()

if __name__ == '__main__':
  main()
