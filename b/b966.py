#我的第一次嘗試，因為超出時間TLE而失敗
n = int(input())
allroute = []
for i in range(n):
    a, b = map(int, input().split())
    allroute.append([a, b])
allroute.sort()
unique = []
for i in allroute:
    if allroute:
        overlap = False
        for j in unique:
            if i[0] <= j[1]:
                if i[1] > j[1]:
                    unique.append([min(i[0], j[0]), i[1]]) #如果只部分重疊，新增新的再刪掉舊的
                    unique.remove(j) #remove()是知道它的值而刪除
                    overlap = True
                else:
                    overlap = True #我們已經把allroute給排序一遍了，我們可以等找到一個獨立的大線段再新增，不需要一直新增刪除
        if overlap == False:
            unique.append(i)
    else:
        unique.append(i)
answer = 0
for u in unique:
    answer += (u[1] - u[0])
print(answer)



#Gemini寫的Answer
n = int(input())
allroute = []
for i in range(n):
    a, b = map(int, input().split())
    allroute.append([a, b])
allroute.sort()
if not allroute:
    print(0)
else:
    merged = []
    curr_start, curr_end = allroute[0] #從第0個跟第1個開始比較
    for i in range(1, n):
        next_start, next_end = allroute[i]
        if next_start <= curr_end: 
            curr_end = max(curr_end, next_end) #如果有重疊，重寫新的線段終點
        else:
            merged.append([curr_start, curr_end])
            curr_start, curr_end = next_start, next_end #如果沒有重疊，加到結果列表裡面，並開始新的線段起點終點
    merged.append([curr_start, curr_end])
    answer = sum(u[1] - u[0] for u in merged) #在for迴圈前面放算出來的數字，再把全部用sum()包起來
    print(answer)





import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if n == 0:
        print(0)
        return
    intervals = []
    for i in range(n):
        intervals.append((int(input_data[1 + i*2]), int(input_data[2 + i*2])))
    intervals.sort()
    total_length = 0
    curr_start, curr_end = intervals[0]
    for i in range(1, n):
        nxt_start, nxt_end = intervals[i]
        if nxt_start <= curr_end:
            if nxt_end > curr_end:
                curr_end = nxt_end
        else:
            total_length += (curr_end - curr_start)
            curr_start, curr_end = nxt_start, nxt_end
    total_length += (curr_end - curr_start)
    sys.stdout.write(str(total_length) + '\n')
if __name__ == '__main__':
    solve()
