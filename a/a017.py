while True:
    try:
        line = input()
        if not line:
            break
        tokens = line.split()
        postfix = []
        operators = []
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '(': 0}
        for token in tokens: #裡面的每個字符
            if token.isdigit(): #是否是數學
                postfix.append(int(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(': #operators裡面有東西，且最後一個不是一個上括號
                    postfix.append(operators.pop()) #pop出最後一個東西
                operators.pop() # 彈出 '('
            else:
                # 處理運算子優先級
                while operators and priority.get(operators[-1], 0) >= priority[token]: #只要
                    postfix.append(operators.pop())
                operators.append(token)
        
        while operators:
            postfix.append(operators.pop())
            
        # --- 步驟 2: 計算後序式 ---
        stack = []
        for token in postfix:
            if isinstance(token, int):
                stack.append(token)
            else:
                b = stack.pop() #刪掉後兩個數字
                a = stack.pop()
                if token == '+': stack.append(a + b) #新增一個數字
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(a // b) # 整數除法
                elif token == '%': stack.append(a % b)
        
        print(stack[0])
        
    except EOFError:
        break
#2+3*4會變成234*+
#2*(3+4)*5會變成234+*5*
