a = list(input("甲方的數字:"))
b = list(input("乙方的數字:"))
text=""
if len(a) != len(b):
    print("輸入長度錯誤!")
for i in range(len(a)):
    if a[i] == "1" and b[i] == "5" or a[i] == "2" and b[i] == "1" or a[i] == "3" and b[i] == "2" or a[i] == "4" and b[i] == "3" or a[i] == "5" and b[i] == "4":
        text += "贏"
    elif a[i] == "5" and b[i] == "1" or a[i] == "1" and b[i] == "2" or a[i] == "2" and b[i] == "3" or a[i] == "3" and b[i] == "4" or a[i] == "4" and b[i] == "5":
        text += "輸"
    elif a[i] == b[i]:
        text += "和"
    else:
        text += "和"
print(text)
