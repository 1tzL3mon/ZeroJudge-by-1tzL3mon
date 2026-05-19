#我自己寫的，遇到TLE執行時間超過限制
h, w = map(int, input().split())
orimap = []
police = []
for i in range(h):
    orimap.append(list(input()))
    for j in range(w):
        if orimap[i][j] == '#':
            police.append([i, j])
result = [['X'] * w for _ in range(h)]
for poly, polx in police:
    result[poly][polx] = '#'
    for ydi, xdi in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        newy = poly + ydi
        newx = polx + xdi
        while newx >= 0 and newx < w and newy >= 0 and newy < h:
            if result[newy][newx] != '#':
                result[newy][newx] = '#'
            newy += ydi
            newx += xdi
for i in range(h):
    print("".join(result[i]))

#Gemini縮短執行時間後的版本
import sys
input_data = sys.stdin.read().split) #sys.stdin.read可以減少執行時間
if input_data:
    h = int(input_data[0])
    w = int(input_data[1])
    has_police_row = [False] * h #因為題目是看警察格子的十字範圍，所以不用記格子，可以只記行跟列
    has_police_col = [False] * w
    for i in range(h):
        row_str = input_data[2 + i] #同一行裡面沒有空格，直接是一個字串
        for j in range(w):
            if row_str[j] == '#': #字串可以直接用[]來取值，不僅限於list
                has_police_row[i] = True
                has_police_col[j] = True
    out = []
    for i in range(h): #逐行進行append
        if has_police_row[i]:
            out.append('#' * w)
        else: #如果該行不是has_police，就把有無警察的列變成一個list之後再append
            row_chars = ['#' if has_police_col[j] else 'X' for j in range(w)]
            out.append("".join(row_chars))
    print("\n".join(out)) #可以在list的每一個字串物件中間加\n輸出






