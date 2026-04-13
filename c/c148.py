from collections import deque #Grok寫的,未完成

INF = 10**9
dx = [0, 1, -1] #dx[0],dx[1],dx[2]分別是向下,向右,向左的x座標改變量
dy = [1, 0,  0] #dy[0],dy[1],dy[2]分別是向下,向右,向左的y座標改變量

def solve(width, height, start_x, goal_x, obstacles):
    if height == 1 and start_x == goal_x: #高度為1,且起點終點重疊
        return 0
    vis = [[[INF] * 3 for _ in range(width)] for _ in range(height)] #創建陣列vis[y][x][方向],之後方向0為下,1為右,2為左
    q = deque() #double-ended queue可以右邊放入,左邊拿出
    y = 0 #設y為0
    testx = start_x + dx[0] #向下走一步
    testy = y + dy[0] #向下走一步
    if 0 <= testy < height and 0 <= testx < width and (testx, testy) not in obstacles: #沒有超過邊框,沒有碰到障礙物
        vis[testy][testx][0] = 0 #走完第一步轉0個彎
        q.append((testx, testy, 0, 0)) #方向向下, 轉0次
        
    for ndir in [1, 2]: #方向右和左
        testx = start_x + dx[ndir] #向右走一步/向左走一步
        testy = y + dy[ndir] #向右走一步/向左走一步
        if 0 <= testx < width and 0 <= testy < height and (testx, testy) not in obstacles: #沒有超過邊框,沒有碰到障礙物
            vis[testy][testx][ndir] = 1  #走完第一步轉1個彎
            q.append((testx, testy, ndir, 1)) #方向向左/右,轉1次
    while q:
        x, y, dir, turns = q.popleft() #左邊拿出,deque變回空的
        testx = x + dx[dir]
        testy = y + dy[dir]
        if 0 <= testx < width and 0 <= testy < height and (testx, testy) not in obstacles:
            if vis[testy][testx][dir] > turns:
                vis[testy][testx][dir] = turns
                q.append((testx, testy, dir, turns))

        for ndir in range(3):
            if ndir == dir:
                continue
            testx = x + dx[ndir]
            testy = y + dy[ndir]
            if 0 <= testx < width and 0 <= testy < height and (testx, testy) not in obstacles:
                if vis[testy][testx][ndir] > turns + 1:
                    vis[testy][testx][ndir] = turns + 1
                    q.append((testx, testy, ndir, turns + 1))
    ans = min(vis[height-1][goal_x])
    return ans if ans < INF else -1

while True:
    try:
        n, m = map(int, input().split())
        b, e = map(int, input().split())
        k = int(input())
        obstacles = set()
        print()
        for _ in range(k):
            x, y = map(int, input().split())
            obstacles.add((x, y))
        result = solve(m, n, b, e, obstacles)
        print(result)
    except:
        break
