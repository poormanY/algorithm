import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/PrimeNumbers'))
from SieveOfEratosthenes import Prime

def main():
  ErrorMsg = "Goldbach's conjecture is wrong."
  p = Prime()
  max_n = 1000000
  li = p.prime_list(max_n)
  for line in sys.stdin:
    n = int(line)
    if n == 0:
      break
    for x in li:
      if x > n/2:
        print(ErrorMsg)
      if p.primes[n-x] == True:
        print("%s = %s + %s" % (n,x,n-x))
        break

main()
