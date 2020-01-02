import sys, string

def main():
  input = sys.stdin.readline
  S = 'baekjoon'
  for s in string.ascii_lowercase:
    i = -1
    if s in S:
      i = S.index(s)
    print(i, end =' ')

main()
