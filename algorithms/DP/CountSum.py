import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from collections import defaultdict
class DP():
  def count(self, n, args=[1,2,3]):
    count = defaultdict(int)
    for x in args:
      count[x] = 1
    for i in range(1, n+1):
      for j in args:
        x = i - j
        count[i] += count[x]
    return count[n]

import sys
def main():
  args = [1,2,3]
  for line in range(11):
    n = int(line)
    d = DP()
    count = d.count(n, args)
    print(count)

if __name__ == '__main__':
  main()
