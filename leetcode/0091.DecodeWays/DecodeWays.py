def numDecodings(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1, -1):
        if s[i] != '0':
            dp[i] = dp[i + 1]
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp[i] += dp[i + 2]

    return dp[0]


if __name__ == "__main__":
    s = "226"
    print(numDecodings(s))
    # 3