n = int(input("請輸入正整數n:"))
num = []
total = 0
for i in range(1,n):
    if n % i == 0:
        num.append(i)
for i in num:
    total += i
if total > n:
    print("abundant")
elif total == n:
    print("perfect")
else:
    print("deficient")
