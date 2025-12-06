while True: #15行
    try:
        days = int(input())
    except:
        break
    enumbers = input().split()
    if len(enumbers) != days:
        break
    sum = 0
    for i in range(days):
        try:
            sum += int(enumbers[i]) * (i+1)
        except:
            break
    print(sum)

#企鵝answer 8行
ip = int(input())
data = input().split()
sum = 0
n = 0
for j in range(1, ip+1): #一樣進行ip次，但從1開始
    sum += j * int(data[n])
    n += 1
print(sum)
