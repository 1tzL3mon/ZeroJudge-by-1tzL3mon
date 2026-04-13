#有deque有set有main的版本
from collections import deque

def solve_maze():
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
        maze = []
        for _ in range(n):
            maze.append(input().strip())
    except EOFError:
        return
    start = (1, 1)
    end = (n - 2, n - 2)
    if maze[start[0]][start[1]] == '#' or maze[end[0]][end[1]] == '#': # 如果起點或終點本身就是障礙物，直接結束
        print("No solution!")
        return
    queue = deque([(start[0], start[1], 1)]) #(列, 行, 目前步數)
    visited = set()
    visited.add(start)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #下、上、右、左的(x,y)移動方向

    while queue:
        r, c, dist = queue.popleft()

        # 到達目的地
        if (r, c) == end:
            print(dist)
            return

        # 嘗試四個方向
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 檢查邊界與是否為路(.)，且尚未造訪過
            if 0 <= nr < n and 0 <= nc < n and \
               maze[nr][nc] == '.' and (nr, nc) not in visited:
                
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    # 若隊列空了仍未找到終點
    print("No solution!")

if __name__ == "__main__":
    solve_maze()



#沒有deque沒有set沒有main的版本
n = int(input())
maze = []
for i in range(n):
    maze.append(list(input())) #list(string)可以把string裡面的每個字變成獨立的物件放在一個列表中

start_r, start_c = 1, 1 #起點的x,y
end_r, end_c = n - 2, n - 2 #終點的x,y

#準備一個「待處理名單」
queue = [[start_r, start_c, 1]] #queue列表裡面會有很多列表，每個列表都有3筆資料

visited = [] #記錄哪些格子走過 (避免原地打轉)
for i in range(n):
    visited.append([False] * n) #有n乘n的裝著False的矩陣
visited[start_r][start_c] = True

found = False
head = 0 # 用來追蹤目前處理到queue中的哪一個列表
while head < len(queue):
    r, c, dist = queue[head]
    head += 1 #這個不是步數，只是處理到第幾個資料，所以每次都會加1
    if r == end_r and c == end_c: #如果這個資料是終點
        print(dist)
        found = True
        break
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n: #if它在邊境內
            if maze[nr][nc] == "." and visited[nr][nc] == False: #if它是"."，而且不是已走過的格子
                visited[nr][nc] = True
                queue.append([nr, nc, dist + 1])
if not found: #如果全部走完都沒找到終點
    print("No solution!")






#我自己默寫的Answer
n = int(input())
maze = []
for _ in range(n):
    line = input()
    row = []
    for j in line:
        row.append(j)
    maze.append(row)

visited = []
for _ in range(n):
    visited.append([False] * n)
visited[1][1] = True

startx, starty = 1, 1
endx, endy = n-2, n-2

task = [[startx, starty, 1]]
found = False
taskathand = 0

while taskathand < len(task):
    x, y, steps = task[taskathand]
    if x == endx and y == endy:
        print(steps)
        found = True
        break
    for directionx, directiony in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newx = x + directionx
        newy = y + directiony
        if newx >= 0 and newx < n and newy >= 0 and newy < n:
            if maze[newx][newy] == '.' and visited[newx][newy] == False:
                visited[newx][newy] = True
                task.append([newx, newy, steps + 1])
    taskathand += 1

if not found:
    print("No solution!")
            
