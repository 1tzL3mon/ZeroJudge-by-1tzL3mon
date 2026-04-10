while True:
    try:
        nums = input()
        ev = 0
        od = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ev += int(nums[i])
            else:
                od += int(nums[i])
        print(abs(ev - od))
    except:
        break
