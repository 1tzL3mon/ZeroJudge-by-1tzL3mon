#如果n是正的就輸出1，如果n是0就輸出0，如果n是負的就輸出-1。不能用if

#不用if
n = int(input())
print((n > 0) - (n < 0))
#boolean也可以被當成數字進行加減法
# True - False = 1
# False - False = 0
# False - True = -1
