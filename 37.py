n,num = int(input("整數:")),[]

while True:
    num.append(n)
    if n == 1:
        break
    elif n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n / 2
for i in range(len(num)):
    print(int(num[i]),end=" ")