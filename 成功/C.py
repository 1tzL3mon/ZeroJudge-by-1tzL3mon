# 1. 讀取第一行 N, M, K, D
first_line = input().split()
n = int(first_line)
m = int(first_line)
k = int(first_line)
d = int(first_line)

# 2. 讀取網格資料
grid = []
for i in range(n):
    row_line = input().split()
    row_ints = []
    for x in row_line:
        row_ints.append(int(x))
    grid.append(row_ints)
dp = []
for i in range(n):
    v_list = []
    for j in range(k + 1):
        v_list.append(-1)
    dp.append(v_list)
INF = 9999999999
for r in range(n):
    val = grid[r][0]
    dp[r][0] = val
    if k >= 1:
        dp[r][1] = INF
for c in range(1, m):
    next_dp = []
    for i in range(n):
        v_list = []
        for j in range(k + 1):
            v_list.append(-1)
        next_dp.append(v_list)
    for r in range(n):
        val = grid[r][c]
        start_r = r - d
        if start_r < 0:
            start_r = 0
        end_r = r + d
        if end_r >= n:
            end_r = n - 1
        for prev_r in range(start_r, end_r + 1):
            for v in range(k + 1):
                if dp[prev_r][v] == -1:
                    continue
                curr_bottleneck = dp[prev_r][v]
                if val < curr_bottleneck:
                    curr_bottleneck = val
                if curr_bottleneck > next_dp[r][v]:
                    next_dp[r][v] = curr_bottleneck
                if v + 1 <= k:
                    curr_bottleneck = dp[prev_r][v]
                    if curr_bottleneck > next_dp[r][v + 1]:
                        next_dp[r][v + 1] = curr_bottleneck
    dp = next_dp
max_ans = -1
for r in range(n):
    for v in range(k + 1):
        if dp[r][v] > max_ans:
            max_ans = dp[r][v]
print(max_ans)
                  
