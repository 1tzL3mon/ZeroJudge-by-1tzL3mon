n = int(input())
h = list(map(int, input().split()))
up = [1] * n
down = [1] * n
for i in range(n):
    for j in range(i):
        if h[i] > h[j]:
            up[i] += down[j]
        if h[i] < h[j]:
            down[i] += up[j]
total_ans = 0
for i in range(n):
    total_ans = total_ans + up[i] + down[i]
ans = total_ans - n
print(ans)

