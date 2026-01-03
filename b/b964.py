n = int(input())
nums = sorted(map(int, input().split()))
print(*(nums)) #中間有空格的string，而不是有逗號的list
fail_max = -1
pass_min = 101
for x in nums: #本身就會由小到大
    if x < 60:
        fail_max = x #直到x大於等於60停止
    elif x >= 60:
        if pass_min == 101: #x剛大於等於60就執行，且只執行一次
            pass_min = x
if fail_max == -1:
    print("best case") #x小於60的情況沒有發生
else:
    print(fail_max)
if pass_min == 101:
    print("worst case") #x大於等於60的情況沒有發生
else:
    print(pass_min)
