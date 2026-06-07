# 字串操作

#Gemini的解法
# 讀取初始字串，並直接轉成字元列表方便操作
s_list = list(input())
k = int(input())
operations = list(map(int, input().split()))
n = len(s_list)
for op in operations:
    # 【操作 0】：兩兩交換 (例如：ab cd -> ba dc)
    if op == 0:
        for i in range(0, n, 2):
            # 交換 i 和 i+1 的位置
            temp = s_list[i]
            s_list[i] = s_list[i+1]
            s_list[i+1] = temp
    # 【操作 1】：兩兩排序 (例如：ba dc -> ab cd)
    elif op == 1:
        for i in range(0, n, 2):
            if s_list[i] > s_list[i+1]:
                temp = s_list[i]
                s_list[i] = s_list[i+1]
                s_list[i+1] = temp
    # 【操作 2】：完美重排 (前半段與後半段交錯組合)
    elif op == 2:
        half = n // 2
        new_list = []
        for i in range(half):
            new_list.append(s_list[i])         # 放左半邊的第 i 個
            new_list.append(s_list[half + i])  # 放右半邊的第 i 個
        s_list = new_list
print("".join(s_list))








import copy #22行
w = input()
times = int(input())
setotwo = list(w)
for t in range(times):
    n = int(input())
    if n == 0:
        for j in range(int(len(setotwo)/2)):
                setotwo[2*j], setotwo[2*j+1] = setotwo[2*j+1], setotwo[2*j]
    elif n == 1:
        for j in range(int(len(setotwo)/2)):
            if str(setotwo[2*j]) > str(setotwo[2*j+1]):
                setotwo[2*j], setotwo[2*j+1] = setotwo[2*j+1], setotwo[2*j]
    elif n == 2:
        halves = copy.deepcopy(setotwo) #copy.deepcopy()的複製不會使用同一個記憶體
        setotwo = []
        for j in range(int(len(w)/2)): #setotwo亂掉,必須要用w
            setotwo.append(halves[j])
            setotwo.append(halves[int(len(w)/2)+j])
for i in range(len(setotwo)):
    print(setotwo[i], end='')
print()


#企鵝answer 19行
ip = input()
text = list(ip)
n = int(input())
for _ in range(n):
    ls = []
    num = int(input())
    if num == 0:
        for i in range(0, len(text), 2):
            ls.append(text[i+1])
            ls.append(text[i])
    elif num == 1:
        pair = sorted([text[i],text[i+1]])
        ls.extend(pair)
    elif num == 2:
        for i in range(0, int(len(text)/2)):
            ls.append(text[i])
            ls.append(text[(int((len(text))/2))+i])
    text = ls #在ls都排序完後,才把text變為ls,這樣text就不會亂掉
print("".join(text)) #把list變成string,且中間沒有空格
