#Gemini的Answer
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append([0] * n) #matrix是n乘n的矩陣
    r, c = 0, 0
    if m == 1: #依序為[右,下,左,上]
        dr = [0, 1, 0, -1] #以向下為正
        dc = [1, 0, -1, 0]
    else: #依序為[下,右,上,左]
        dr = [1, 0, -1, 0] #以向下為正
        dc = [0, 1, 0, -1]
    di = 0 #從列表中的[0]開始
    for num in range(1, n * n + 1): #執行n乘n次
        matrix[r][c] = num
        if num == n * n:
            break #如果是最後一次，跳過後面的步驟
        nr = r + dr[di] #上下座標照著列表dr還有當下的di設下一步要走的座標nr
        nc = c + dc[di]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or matrix[nr][nc] != 0: #如果超出上面，或超出下面，或超出左邊，或超出右邊，或要走的座標被填過了
            di = (di + 1) % 4 #改變方向，每次加1，到4的時候自動歸0
            nr = r + dr[di] #重新設定下一步要走的座標nr
            nc = c + dc[di]
        r, c = nr, nc #把要填的座標設為nr和nc
    for row in matrix: #有n個
        row_str = ""
        for val in row:
            row_str += "%5d" % val #5個空格，加上一個數字
        print(row_str) #會列印n次


#自己默寫一遍的Answer
i = int(input())
for _ in range(i):
    side, spiral = map(int, input().split())
    matrix = []
    for u in range(side):
        matrix.append([0]*side)
    if spiral == 1:
        vertmove = [1, 0, -1, 0]
        horimove = [0, 1, 0, -1]
    else:
        vertmove = [0, 1, 0, -1]
        horimove = [1, 0, -1, 0]
    waytomove = 0
    x, y = 0, 0
    for i in range(1, side*side+1):
        matrix[x][y] = i
        nextx = x + horimove[waytomove]
        nexty = y + vertmove[waytomove]
        if nextx >= side or nextx < 0 or nexty >= side or nexty < 0 or matrix[nextx][nexty] != 0:
            waytomove = (waytomove + 1) % 4
            nextx = x + horimove[waytomove]
            nexty = y + vertmove[waytomove]
        x, y = nextx, nexty
    for row in matrix:
        rowprint = ''
        for numbers in row:
            if (numbers // 10000) > 0: #空格有不同長度，用if來決定
                rowprint += ' '*0
            elif (numbers // 1000) > 0:
                rowprint += ' '*1
            elif (numbers // 100) > 0:
                rowprint += ' '*2
            elif (numbers // 10) > 0:
                rowprint += ' '*3
            else:
                rowprint += ' '*4
            rowprint += str(numbers)
        print(rowprint)
