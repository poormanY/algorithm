import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/PrimeNumbers'))
from SieveOfEratosthenes import Prime

def main():
  input = sys.stdin.readline
  N = int(input())
  numbers = list(map(int,input().split()))

  p = Prime()
  p.execute(max(numbers))
  count = 0
  for n in numbers:
    if p.primes[n] == True:
      count += 1
  print(count)

main()
