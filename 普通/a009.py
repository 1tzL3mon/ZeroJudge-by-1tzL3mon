while True:
    try:
        s = input()
        ans = ""
        for char in s:
            new_char = chr(ord(char) - 7) #用ord()把文字變成數字，減掉7，再用chr()把數字變成文字
            ans += new_char
        print(ans)
    except:
        break
