same,text = [],""
string_a = list(input("請輸入string_a:"))
string_b = list(input("請輸入string_b:"))
for i in range(len(string_a)):
    if string_a[i] in string_b and string_a[i] not in same:
        same.append(string_a[i])
same.sort()
for i in same:
    text += i
if text == "":
    print("N")
else:
    print(text)