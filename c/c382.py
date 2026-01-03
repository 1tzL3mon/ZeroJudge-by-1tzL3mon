while True:
    try:
        whole = input()
        if '+' in whole: #檢查字符是否在string裡面
            nums = whole.split('+')
            print(int(nums[0])+int(nums[1]))
        elif '-' in whole:
            nums = whole.split('-')
            print(int(nums[0])-int(nums[1]))
        elif '*' in whole:
            nums = whole.split('*')
            print(int(nums[0])*int(nums[1]))
        else:
            nums = whole.split('/')
            print(int(int(nums[0])/int(nums[1])))
    except:
        break
