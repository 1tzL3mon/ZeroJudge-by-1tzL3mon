# 兩個正整數n,D，下一行有n個整數
# 第一個股票一定會買x，遇到價格y大於等於x+D時即賣出，並轉得利潤y-x
# 若當下沒有持有股票且上一次的賣出價格為y，當遇到價格x小於等於y-D時則會買進股票x


while True:
    try:
        t, d = map(int, input().split())
        his = list(map(int, input().split()))
        x = his[0]
        hav = 1
        fin = 0
        for i in range(1, t):
            if hav == 1 and his[i] >= (x + d):
                fin += (his[i] - x)
                x = his[i]
                hav = 0
            elif hav == 0 and his[i] <= (x - d):
                x = his[i]
                hav = 1
        print(fin)
    except:
        break


# Gemini的解法，跟我的一模一樣
n, d = map(int, input().split())
prices = list(map(int, input().split()))
total_profit = 0
last_price = prices[0]
has_stock = True
for i in range(1, n):
    current_price = prices[i]
    if has_stock:
        if current_price >= last_price + d:
            total_profit = total_profit + (current_price - last_price)
            last_price = current_price
            has_stock = False
    else:
        if current_price <= last_price - d:
            last_price = current_price
            has_stock = True
print(total_profit)
