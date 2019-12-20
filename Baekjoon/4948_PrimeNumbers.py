import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/PrimeNumbers'))
from SieveOfEratosthenes import Prime

def main():
  p = Prime()
  for line in sys.stdin:
    n = int(line)
    if n == 0:
      break
    start = n + 1
    end = n * 2
    print(len(p.prime_list(start=start, end=end)))

main()
