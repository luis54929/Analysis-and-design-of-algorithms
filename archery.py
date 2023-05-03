#Problem 12840: https://onlinejudge.org/external/128/12840.pdf

def min_arrows(P, S):
    N = len(P)
    dp = [float('inf')] * (S + 1)
    dp[0] = 0
    for i in range(1, S + 1):
        for j in range(N):
            if i >= P[j]:
                dp[i] = min(dp[i], dp[i - P[j]] + 1)
    if dp[S] == float('inf'):
        return []
    result = []
    while S > 0:
        for j in range(N-1, -1, -1):
            if S >= P[j] and dp[S - P[j]] == dp[S] - 1:
                result.append(P[j])
                S -= P[j]
                break
    return sorted(result, reverse=True)
  
def main():
  T = int(input())
  for t in range(T):
      N, S = map(int, input().split())
      P = list(map(int, input().split()))
      result = min_arrows(P, S)
      if not result:
          print(f'Case {t+1}: impossible')
      else:
          print(f'Case {t+1}: [{len(result)}] {" ".join(map(str, result))}')
main()