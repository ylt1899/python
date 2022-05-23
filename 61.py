min,second = input("請輸入遊戲時間:").split(":")
play_time,time,count = 0,0,0
play_time = int(min)*60 + int(second) -75
time = int(play_time / 30) + 1
for i in range(time):
    if (i+1) % 3 == 0:
        if (i+1) % 2 == 0:
            count += 7-1
        else:
            count += 7 
    else:
        if (i+1) % 2 == 0:
            count += 6-1
        else:
            count += 6
print("%d隻兵" %(count))

