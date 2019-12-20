import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/PrimeNumbers'))
from SieveOfEratosthenes import Prime

def main():
  input = sys.stdin.readline
  M, N = list(map(int,input().split()))
  p = Prime()
  for x in p.prime_list(N, M):
    print(x)

main()
