size = int(input("請輸入陣列大小:"))
ll = []
biggest = []
location = []
for i in range(size):
    a = input().split(" ")
    ll.append(a)
for i in range(3):
    biggest.append(0)
    location.append("0")

for i in range(size):
    for j in range(size):
        if int(ll[i][j]) > biggest[0]:
            biggest[0] = int(ll[i][j]) 
            location[0] = "("+str(i+1)+","+str(j+1)+")" 
        elif int(ll[i][j]) > biggest[1]:
            biggest[1] = int(ll[i][j]) 
            location[1] = "("+str(i+1)+","+str(j+1)+")" 
        elif int(ll[i][j]) > biggest[2]:
            biggest[2] = int(ll[i][j])
            location[2] = "("+str(i+1)+","+str(j+1)+")" 
print("最大值為:%d" % (biggest[0]+biggest[1]+biggest[2]))
print("位置為:"+location[0]+","+location[1]+","+location[2])
