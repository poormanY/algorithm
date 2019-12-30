import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/PrimeNumbers'))
from SieveOfEratosthenes import Prime

def isPalindrome(s):
  if s == s[::-1]:
    return True
  else:
    return False

# Main Function
import sys
def main():
  N = int(sys.stdin.readline())
  p = Prime()
  start = N
  end = 1003001 #1000000이상의 소수&팰린드롬
  for x in p.prime_list(start=start, end=end):
    if isPalindrome(str(x)):
      print(x)
      break

main()
