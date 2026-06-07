#Gemini的快速確認方法
s = input()
left = 0
right = len(s) - 1
is_palindrome = True #預設它是迴文
while left < right: #只要正在比較的兩個數字真的是right在右邊，left在左邊就繼續比較
    if s[left] != s[right]:
        is_palindrome = False
        break  #既然已經不是了，就直接跳出迴圈
    left = left + 1
    right = right - 1
if is_palindrome:
    print("yes")
else:
    print("no")



#Gemini的高級解法
def is_palindrome(s):
    return s == s[::-1]
a = input()
print(is_palindrome(a))
