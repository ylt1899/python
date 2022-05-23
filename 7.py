tt , time = input("輸入月租型式及通話時間為:").split(",")
num_tt = int(tt)
num_time = int(time)
money = 0.0
if num_tt == 186:
    money = num_time * 0.09
    if money >= 186:
        money = money*0.8
    else:
        money = money*0.9
elif num_tt == 386:
    money = num_time * 0.08
    if money > 386:
        money = money *0.7 
    else:
        money = money*0.8
elif num_tt == 586:
    money = num_time * 0.07
    if money >= 586:
        money = money*0.6 
    else:
        money = money*0.7
elif num_tt == 986:
    money = num_time * 0.06
    if money >= 986:
        money = money*0.5
    else:
        money = money*0.6
else:
    print("輸入錯誤")
print("通話費為:" + "%.0f"%money)


