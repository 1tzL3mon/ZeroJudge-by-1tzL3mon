n = int(input())
all_nums = map(int, input().split())
counts = {}
for x in all_nums:
    counts[x] = counts.get(x, 0) + 1 #dictionary.get(key, 0)如果沒有key物件就會創造一個value為0的key物件，並加1
max_freq = max(counts.values()) #dictionary.value()可以變成字典值的物件，這個物件可以取max()值
for x in sorted(counts.keys()): #依據dictionary.key()的順序執行
    if counts[x] == max_freq: #dictionary[key]取得value
        print(x, max_freq)

#企鵝answer
n = int(input())
ls = list(map(int, input().split()))
ls.sort()
dict = {}
for item in ls:
    if item in dict:
        dict[item] += 1 #如果有item就加1
    else:
        dict[item] = 1 #如果沒有就設1
mx = max(dict.values())
for item in dict:
    if str(dict.get(item)) == str(mx): #dictionary.get(key)取得value
        print(str(item), str(mx))
