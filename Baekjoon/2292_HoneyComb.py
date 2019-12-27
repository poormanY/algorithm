# 1 : 1 0
# 2 : 2-7 6
# 3 : 8-19 12
# 4 : 20-37 18
# 5 : 38-61 24
# f(x) = f(x-1) + 6*(x-1)

class HoneyComb():
  def count(self, n):
    x = 1
    diff = 6
    cnt = 0
    while(True):
      x += diff*cnt
      cnt += 1
      if (n <= x):
        return cnt

import sys
def main():
  input = sys.stdin.readline
  N = int(input())
  
  hb = HoneyComb()
  cnt = hb.count(N)
  print(cnt)

main()
