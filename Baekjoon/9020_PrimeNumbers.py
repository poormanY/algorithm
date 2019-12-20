import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/PrimeNumbers'))
from SieveOfEratosthenes import Prime

def main():
  T = int(sys.stdin.readline())

  p = Prime()
  max_n = 1000000
  li = p.prime_list(max_n)
  for line in sys.stdin:
    n = int(line)
    for x in range(n//2,1,-1):
      if (p.primes[x] == True) and (p.primes[n-x] == True):
        print(' '.join(map(str,[x,n-x])))
        break
main()
