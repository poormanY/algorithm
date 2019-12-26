import collections
class Words():
  def most_common(self, word, n=2):
    c = collections.Counter(word)
    return c.most_common(n)

import sys
def main():
  input = sys.stdin.readline
  s = input().strip()
  w = Words()
  lst = w.most_common(s.upper())
  vals = list(map(lambda x: x[1], lst))
  if vals[0] == vals[1]:
    print('?')
  else:
    print(lst[0][0])

main()
