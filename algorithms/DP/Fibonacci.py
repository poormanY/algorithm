import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class DP():
  def fibonacci(self, n):
    x, y = 0, 1
    for i in range(n):
      x, y = y, x+y
    return x

def main():
  d = DP()
  for i in range(10):
    f = d.fibonacci(i)
    print(f)

if __name__ == '__main__':
  main()
