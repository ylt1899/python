dic = {}
time = int(input("輸入比數:"))
for i in range(time):
    kk,yy = input().split(" ")
    dic.update({kk:yy})
for key,value in dic.items():
    print(key+"牌得到"+value+"面")