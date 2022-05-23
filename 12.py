num = input("輸入一整數序為:").split(" ")
list_copy = []
time = 0
TorF = 0
ans = ""
for i in range(len(num)):
    if num[i] not in list_copy:
        list_copy.append(num[i])
for i in range(len(list_copy)):
    time = 0
    for j in range(len(num)):
        if list_copy[i] == num[j]:
            time += 1
    if time > (len(num)/2):
        ans = list_copy[i]
        TorF = 1
        break
if TorF == 1:
    print("過半元素為:" + ans)
else:
    print("過半元素為:No")
