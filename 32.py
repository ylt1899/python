M = int(input("小明身上有幾元:"))
N = int(input("販賣機有幾種飲料:"))
drink = []
howmany = 0
if M > 100 or M < 0 or N < 1 or N > 30:
    print('輸入錯誤!')
for i in range(N):
    drink.append(int(input()))
for i in range(len(drink)):
    if M >= drink[i]:
        howmany += 1
print(howmany)