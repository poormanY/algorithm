import sys
def main():
  input = sys.stdin.readline
  N = int(input())
  dp = list(map(int, input().split()))
  for line in sys.stdin:
    rgb = list(map(int, line.split()))
    rgb[0] += min(dp[1], dp[2])
    rgb[1] += min(dp[0], dp[2])
    rgb[2] += min(dp[0], dp[1])
    dp = rgb
  print(min(dp))

main()
