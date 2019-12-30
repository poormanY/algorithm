'''
N제한이 100,000,000 이므로 좌우가 똑같다는 팰린드롬의 성질을 이용하여

최대 10,000번까지 돌면서 팰린드롬을 먼저 다 만들어 둔 다음

sqrt(N) 만큼 돌면서 소수체크를 해서 출력
'''
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
input = sys.stdin.readline
def main():
  start, end = map(int, input().split())
  p = Prime()
  for x in p.prime_list(start=start, end=end):
    if isPalindrome(str(x)):
      print(x)
  print(-1)

main()
