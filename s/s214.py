#我的第一次嘗試，因為超出時間而失敗
height, length, amount, time = map(int, input().split())
plate = []
for _ in range(height):
    plate.append(list(map(int, input().split())))
for t in range(1, time+1):  #每一次跑就是跑整張地圖，因此有三重for迴圈
    atthesametime = [[False] * length for _ in range(height)]
    for h in range(height):
        for l in range(length):
            if plate[h][l] <= amount and plate[h][l] > 0:
                if h > 0:
                    if plate[h-1][l] != -1:
                        if plate[h-1][l] != 0 and atthesametime[h-1][l] == True:
                            plate[h-1][l] = min(plate[h-1][l], plate[h][l])
                        elif plate[h-1][l] == 0:
                            plate[h-1][l] = plate[h][l]
                            atthesametime[h-1][l] = True
                if h < (height-1):
                    if plate[h+1][l] != -1:
                        if plate[h+1][l] != 0 and atthesametime[h+1][l] == True:
                            plate[h+1][l] = min(plate[h+1][l], plate[h][l])
                        elif plate[h+1][l] == 0:
                            plate[h+1][l] = plate[h][l]
                            atthesametime[h+1][l] = True
                if l > 0:
                    if plate[h][l-1] != -1:
                        if plate[h][l-1] != 0 and atthesametime[h][l-1] == True:
                            plate[h][l-1] = min(plate[h][l-1], plate[h][l])
                        elif plate[h][l-1] == 0:
                            plate[h][l-1] = plate[h][l]
                            atthesametime[h][l-1] = True
                if l < (length-1):
                    if plate[h][l+1] != -1:
                        if plate[h][l+1] != 0 and atthesametime[h][l+1] == True:
                            plate[h][l+1] = min(plate[h][l+1], plate[h][l])
                        elif plate[h][l+1] == 0:
                            plate[h][l+1] = plate[h][l]
                            atthesametime[h][l+1] = True
answer = [0] * amount
for h in range(height):
    for l in range(length):
        if plate[h][l] <= amount and plate[h][l] > 0:
            answer[(plate[h][l] - 1)] += 1
print(*answer)




h, l, m, t = map(int, input().split())
plate = []
for _ in range(h):
    plate.append(list(map(int, input().split())))
current_sources = []
for r in range(h):
    for c in range(l):
        if 0 < plate[r][c] <= m:
            current_sources.append((r, c, plate[r][c])) #顯跑完一次h乘l的地圖，紀錄所有源頭
for _ in range(t):
    if not current_sources:
        break
    current_sources.sort(key=lambda x: x[2]) #current_scores裡面有x，x的[2]是細菌編號，冒號左邊是輸入，右邊是輸出
    next_sources = []
    temp_changes = {} #temp_changes是一個字典
    for r, c, color in current_sources:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #只跑目前的源頭，和源頭的四個方向
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < l:
                if plate[nr][nc] == 0:
                    if (nr, nc) not in temp_changes or color < temp_changes[(nr, nc)]: #如果它不在字典裡面，或字典裡的數字比較大
                        temp_changes[(nr, nc)] = color
    for (nr, nc), color in temp_changes.items():
        plate[nr][nc] = color #用字典來調整地圖
        next_sources.append((nr, nc, color)) #把它加到一個分開的next_sources列表
    current_sources = next_sources
answer = [0] * m
for r in range(h):
    for c in range(l):
        val = plate[r][c]
        if 0 < val <= m:
            answer[val - 1] += 1
print(*answer)





from collections import deque
h, l, m, t = map(int, input().split())
plate = []
for _ in range(h):
    plate.append(list(map(int, input().split())))
que = deque()
initial_bacteria = []
for r in range(h):
    for c in range(l):
        if 0 < plate[r][c] <= m:
            initial_bacteria.append((r, c, plate[r][c], 0))
initial_bacteria.sort(key=lambda x: x[2])
for b in initial_bacteria:
    que.append(b)
while que:
    r, c, color, curr_t = que.popleft()
    if curr_t >= t:
        continue
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        
        # 判斷是否在邊界內
        if 0 <= nr < h and 0 <= nc < l:
            # 只有「空地 (0)」可以被佔領
            if plate[nr][nc] == 0:
                plate[nr][nc] = color
                # 佔領後，這個新點成為下一秒的擴散源，放進隊列
                que.append((nr, nc, color, curr_t + 1))

# 5. 統計結果
answer = [0] * m
for r in range(h):
    for c in range(l):
        val = plate[r][c]
        if 0 < val <= m:
            answer[val - 1] += 1

# 6. 輸出
print(*answer)
