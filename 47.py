dic = []
time = int(input("輸入比數:"))
for i in range(time):
    kk,yy = input().split(" ")
    dic.append([kk,yy])
for i in range(len(dic)):
    print(dic[i][0]+"牌得到"+dic[i][1]+"面")