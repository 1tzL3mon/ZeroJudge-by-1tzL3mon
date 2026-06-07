# 輸出兩個數字差的絕對值
# 範例輸入1   I I
#            MM II
#            #
#範例輸出1   ZERO
#            MCMXCVIII

#Gemini的答案
roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} #字典，在把羅馬數字變成阿拉伯數字時會用到
def to_int(s): #把一個沒有空格的字串變成數字
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]: #如果i不是最後一位，且i的數字小於i+1的數字
            res -= roman_map[s[i]] #總和減掉i的數字
        else:
            res += roman_map[s[i]] #如果not，就加上i的數字
    return res


def to_roman(n):
    if n == 0: return "ZERO"
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] #非常重要，直接把900當成一個特殊寫法寫在交換表裡面
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for i in range(len(val)): #有十三個羅馬數字，會執行十三遍
        while n >= val[i]: #大於1000就會扣1000，直到小於為止，並換下一個數字
            res += syb[i]
            n -= val[i]
    return res


while True:
    line = input().split()
    if line[0] == "#": #如果開頭是井字號，結束程式
        break
    num1 = to_int(line[0])
    num2 = to_int(line[1])
    diff = abs(num1 - num2) #兩個數字的差的絕對值，直接在把它們變成數字後用-和abs()來處理就好
    print(to_roman(diff))
