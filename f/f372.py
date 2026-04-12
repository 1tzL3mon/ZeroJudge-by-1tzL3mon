#我的錯誤答案
while True:
    try:
        minutes = int(input())
        if (3**minutes) > 10006: #如果不用pow()功能，數字可能太大無法取餘數
            print((3**minutes) % 10007)
        else:
            print(3**minutes)
    except:
        break

#Gemini正確答案
while True:
    try:
        minutes = int(input())
        ans = pow(3, minutes, 10007) #3的minutes次方，取10007的餘數
        print(ans)
    except:
        break
