import sys
input = sys.stdin.readline
from collections import defaultdict

import os
sys.path.append(os.path.abspath('../algorithm/algorithms/PrimeNumbers'))
from SieveOfEratosthenes import Prime

def main():
  M, N = list(map(int,input().split()))
  p = Prime()
  for x in p.prime_list(N, M):
    print(x)

main()
