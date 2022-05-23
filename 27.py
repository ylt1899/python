num = list(input("輸入整數數列(end結束):"))
list_num = []
oo = [""]
for i in range(len(num)):
    for j in range(len(num)):
        list_num.append(num[i:j+1])
for i in range(len(list_num)):
    if list_num[i] == list_num[i][::-1] and len(list_num[i]) > len(oo):
        oo = list_num[i]
print(oo)

