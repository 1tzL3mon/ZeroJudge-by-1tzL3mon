t_str = input()
if t_str:
    t = int(t_str)
    for _ in range(t):
        line = input().split()
        n = int(line[0])
        m = int(line[1])
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        r, c = 0, 0
        if m == 1:
            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]
        else:
            dr = [1, 0, -1, 0]
            dc = [0, 1, 0, -1]
        di = 0
        for num in range(1, n * n + 1):
            matrix[r][c] = num
            if num == n * n:
                break
            nr = r + dr[di]
            nc = c + dc[di]
            if nr < 0 or nr >= n or nc < 0 or nc >= n or matrix[nr][nc] != 0:
                di = (di + 1) % 4
                nr = r + dr[di]
                nc = c + dc[di]
            r, c = nr, nc
        for row in matrix:
            row_str = ""
            for val in row:
                row_str += "%5d" % val
            print(row_str)
