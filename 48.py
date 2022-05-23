dic = {}
time = int(input("輸入筆數:"))
for i in range(time):
    kk,yy = input().split(" ")
    dic.update({kk:yy})
check = input("輸入欲查詢單字:")
for key,value in dic.items():
    if key == check:
        print(key+"中文意思為"+value)
        break