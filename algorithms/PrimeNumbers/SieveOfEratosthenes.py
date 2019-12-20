import sys
import io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from collections import defaultdict

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# 에라토스테네스의 체
class Prime:
  def __init__(self):
    self.primes = defaultdict(lambda: True)
    self.primes[1] = False

  def execute(self, end, start=2):
    m = int(end ** 0.5)
    for i in range(2, m+1):
      if self.primes[i] == True:
        for j in range(i+i, end+1, i):
          self.primes[j] = False

  def prime_list(self, end, start=2):
    self.execute(end, start)
    return [i for i in range(start,end+1) if self.primes[i] == True]

# Main Function
def main():
  p = Prime()
  start = 1
  end = 100
  x = p.prime_list(start=start, end=end)
  print(len(x), x)

if __name__ == '__main__':
  main()
