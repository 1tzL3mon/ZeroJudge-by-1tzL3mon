try:
    n = int(input())
    if n == 1:
        print("0\n0")
    else:
        diffs = sorted(map(int, input().split())) #一輸入就sorted
        
        mx = diffs.pop() #刪除最後一個
        res = [0, mx]
        stack = [(diffs, res)]
        final_res = []

        while stack:
            curr_diffs, curr_res = stack.pop()
            
            if not curr_diffs:
                final_res = curr_res
                break
            
            target = curr_diffs[-1]
            for x in [target, mx - target]:
                if x in curr_res: continue
                needed = [abs(x - item) for item in curr_res]
                temp_d = curr_diffs[:]
                possible = True
                for d in needed:
                    if d in temp_d:
                        temp_d.remove(d)
                    else:
                        possible = False
                        break
                
                if possible:
                    stack.append((temp_d, curr_res + [x]))

        ans = sorted(final_res)
        print(*(ans))
        print(*(mx - i for i in reversed(ans)))
except:
    break
