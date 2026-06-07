#兩個半小時，X、Y以空白區隔，代表現在時間是X:Y
#範例輸入   9 30
#範例輸出   12:00

#Gemini的手動補0方法
h, m = map(int, input().split())
total_minutes = h * 60 + m
total_minutes = total_minutes + 150
new_h = (total_minutes // 60) % 24
new_m = total_minutes % 60
if new_h < 10:
    str_h = "0" + str(new_h)
else:
    str_h = str(new_h)
if new_m < 10:
    str_m = "0" + str(new_m)
else:
    str_m = str(new_m)
print(str_h + ":" + str_m)


#Gemini的高級解法
h, m = map(int, input().split())
total_minutes = h * 60 + m
total_minutes = total_minutes + 150
new_h = (total_minutes // 60) % 24
new_m = total_minutes % 60
# 4. 格式化輸出（不足兩位數自動補 0）
# :02d 的意思是：這是一個整數(d)，寬度為 2 位，不足的話前面補 0
print(f"{new_h:02d}:{new_m:02d}")
