time = int(input("搭了幾次電梯:"))
money,last = 0,1
for i in range(time):
    floor = int(input())
    if floor == last or time > 10 or time < 1:
        print("輸入錯誤!")
    if floor > last:
        money += (floor - last)*20
    elif floor < last:
        money += (last - floor)*10
    last = floor
print(str(money) + "元")
