dic = {}
time = int(input("輸入n值:"))
for i in range(time):
    name = input("請輸入姓名:")
    e_mail = input("請輸入電子信箱:")
    dic.update({name:e_mail})
find = input("請輸入要查詢電子郵件的姓名:")
print(find + "電子郵件帳號為" + dic[find]) 



