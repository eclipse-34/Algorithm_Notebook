# DP, 실버3
n = int(input())
s = [int(input()) for i in range(n)]
s.insert(0, 0)
dp = [0] * (n + 1)
if n <= 2:
    print(sum(s))
else:
    dp[1] = s[1]
    dp[2] = s[1] + s[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + s[i - 1], dp[i - 2]) + s[i]
    print(dp[n])
