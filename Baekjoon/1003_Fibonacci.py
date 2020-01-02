import sys

def main():
  input = sys.stdin.readline
  T = int(input())
  for line in sys.stdin:
    N = int(line)
    x = [1,0]
    y = [0,1]
    for i in range(N):
      x, y = y, [x[0]+y[0], x[1]+y[1]]
    print(' '.join(map(str, list(x))))

main()
