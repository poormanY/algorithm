#4
#10 8 5 7 9
#10 9 10 9 5
#10 3 5 9 10
#1 2 3 6 9

class Score():
  def __init__(self):
    self.kin_score = 4
    self.kin_print = 'KIN'

  def eval(self, lst):
    lst_sort = list(sorted(lst))[1:-1]
    if max(lst_sort) - min(lst_sort) >= self.kin_score:
      return self.kin_print
    else:
      return sum(lst_sort)

import sys
def main():
  input = sys.stdin.readline
  N = int(input())
  for line in sys.stdin:
    lst = list(map(int, line.split()))
    sc = Score()
    val = sc.eval(lst)
    print(val)

main()
