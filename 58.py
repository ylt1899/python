num,biggest,small = [],[0,0,0],[10000,10000,10000]
for i in range(10):
    nn = int(input("請輸入第%d個數字:" % (i+1))) 
    num.append(nn)
for i in range(10):
    if num[i] > biggest[0]:
        biggest[2] = biggest[1]
        biggest[1] = biggest[0]
        biggest[0] = num[i]
    elif num[i] < biggest[0] and num[i] > biggest[1]:
        biggest[2] = biggest[1]
        biggest[1] = num[i]
    elif num[i] < biggest[0] and num[i] < biggest[1] and num[i] > biggest[2]:
        biggest[2] = num[i]

    if num[i] < small[2]:
        small[0] = small[1]
        small[1] = small[2]
        small[2] = num[i]
    elif num[i] > small[2] and num[i] < small[1]:
        small[0] = small[1]
        small[1] = num[i]
    elif num[i] > small[2] and num[i] > small[1] and num[i] < small[0]:
        small[0] = num[i]
print("最大的3個數字為:%d,%d,%d" % (biggest[0],biggest[1],biggest[2]))
print("最小的3個數字為:%d,%d,%d" % (small[0],small[1],small[2]))