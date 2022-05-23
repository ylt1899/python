dic = {"1":72,"2":62,"3":82,"4":44,"5":60,"A":55,"B":68}
choose = list(input("請選擇主餐及升級的套餐:"))
drink = input("是否升級成大杯飲料:")
big = input("是否換成大薯:")
money = 0
if len(choose) > 1:
    money += dic[choose[0]] + dic[choose[1]]
else:
    money += dic[choose[0]]
if drink == "是":
    money += 7
if big == "是":
    money += 13
print("總共為%d元" %(money))