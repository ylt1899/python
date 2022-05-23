num1 = int(input("請輸入第一個要判斷的數字:"))
num2 = int(input("請輸入第二個要判斷的數字:"))
TorF = 1
if num1 - num2 == 2 or num1 - num2 == -2:
    for i in range(2,num1):
        if num1 % i == 0:
            TorF = 0
            break
        else:
            TorF = 1
    for i in range(2,num2):
        if num2 % i == 0:
            TorF = 0
            break
        else:
            TorF = 1
    if TorF == 1:
        print("Y")
    else:
        print("N")
else:
    print("N")
