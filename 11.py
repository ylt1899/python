str_month,str_day = input("輸入月及日:").split(" ")
month = int(str_month)
day = int(str_day)
if month == 1 and day >=21 or month == 2 and day <= 18:
    print("水瓶")
elif month == 2 and day >= 19 or month == 3 and day <= 20:
    print("雙魚")
elif month == 3 and day >= 21 or month == 4 and day <= 20:
    print("牡羊")
elif month == 4 and day >= 21 or month == 5 and day <= 21:
    print("金牛")
elif month == 5 and day >= 22 or month == 6 and day <= 21:
    print("雙子")
elif month == 6 and day >= 22 or month == 7 and day <= 22:
    print("巨蠍")
elif month == 7 and day >= 23 or month == 8 and day <= 23:
    print("獅子")
elif month == 8 and day >= 24 or month == 9 and day <= 23:
    print("處女")
elif month == 9 and day >= 24 or month == 10 and day <= 23:
    print("天秤")
elif month == 10 and day >= 24 or month == 11 and day <= 22:
    print("天蠍")
elif month == 11 and day >= 23 or month == 12 and day <= 21:
    print("射手")
elif month == 12 and day >= 22 or month == 1 and day <= 20:
    print("魔羯")