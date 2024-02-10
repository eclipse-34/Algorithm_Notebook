def solution(n):
    answer = 0
    dp = [0] * (n + 3)
    dp[1] = 1
    dp[2] = 2
    if n < 3:
        answer = dp[n]
    else:
        for i in range(3, n + 1):
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007
        answer = dp[n]
    return answer