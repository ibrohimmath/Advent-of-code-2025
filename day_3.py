def first():
    lines = open("input.txt", "r").read().splitlines()

    sum = 0
    for line in lines:
        mxNumber, mxDig = -1, -1
        for i in range(len(line) - 1, -1, -1):
            dig = int(line[i])
            if mxDig > -1:
                mxNumber = max(mxNumber, 10 * dig + mxDig)
            mxDig = max(mxDig, dig)
        sum += mxNumber
    print(sum)

def second():
    lines = open("input.txt", "r").read().splitlines()

    sum = 0
    for line in lines:
        N = len(line) 
        dp = [[0] * 12 for _ in range(N)] 
        for i in range(N - 1, -1, -1):
            dig = int(line[i])
            for j in range(min(N - i, 12)):
                dp[i][j] = dig * 10**j + (dp[i + 1][j - 1] if i + 1 < N and j > 0 else 0)
                if i + 1 < N:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j])
        sum += dp[0][-1]
    print(sum)

second()

