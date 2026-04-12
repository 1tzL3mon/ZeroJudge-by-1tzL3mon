













#企鵝answer
while True:
    try:
        a, b, n = map(int, input().split()) #n為小數點後第幾位
        it = a//b #it為a除以b的整數部分
        f = a%b #f為a除以b的餘數
        ls = []
        for _ in range(n):
            f *= 10 #先算一個小數點後的位，餘數乘以10
            ls.append(str(f//b)) #可以除的，變成小數點後的其中一位
            f %= b #沒辦法除的，f設為新的餘數，繼續往下
        if n == 0:
            print(it)
        else:
            print(f"{it}."+ "".join(ls))
    except EOFError:
        break
