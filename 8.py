long = int(input("輸入第一行正整數為:"))
num = input("第二行中數列中的數字為:").split(" ")
num2 = [] #set陣列
moreTime_num = 0 #計算最大值
more_time = 0    #計算最大次數
time = 0
if len(num) == long:
    for i in range(len(num)):
        if num[i] not in num2:
            num2.append(num[i])

    for i in range(len(num2)):
        time = 0
        for j in range(len(num)):
            if num2[i] == num[j]:
                time += 1
            
            if time > more_time:
                moreTime_num = num2[i]
                more_time = time
    if more_time == 1:
        print("每個數字剛好只出現1次")
    else:
        print("最大出現次數的數字為:"+ str(moreTime_num))
        print("出現次數為:"+str(more_time))
else:
    print("輸入錯誤")
