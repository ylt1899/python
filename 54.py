km,money = float(input("請輸入路程公里數(km):"))*1000,75
print(km)
if km < 1500:
    money = money
elif km > 1500:
    km -= 1500
if km > 250:
    if km % 250 == 0:
        money += int(km/250)*5
    else:
        money += int(km/250)*5 + 5
else:
        money += 5
print("所需車資為:%d" % (money))
