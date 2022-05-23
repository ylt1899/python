n = int(input())
strat,num,all = 0,2,[]
if n % 2 == 1:
    start = 1
else:
    start = 2
while start != n:
    all.append(start)
    start += num
all.append(n)
for i in range(len(all)):
    if i < len(all)-1:
        for j in range(len(all)-1):
            print(" ",end="")
        print(all[i])
    elif i == len(all)-1:
        for j in all:
            print(j,end="")
        for j in all[len(all)-2::-1]:
            print(j,end="")
print()
for i in all[len(all)-2::-1]:
    for j in range(len(all)-1):
        print(" ",end="")
    print(i)

            


