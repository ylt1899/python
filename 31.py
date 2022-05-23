a,b = input("輸入矩陣的維度:").split(" ")
one,two,oo = [],[],[]
print(a+b)
for i in range(2):
    if i == 0:
        for j in range(int(a)):
            one.append(input().split(" "))
    else:
        for j in range(int(a)):
            two.append(input().split(" "))
print(len(one))
print(len(two))
for i in range(int(a)):
    copy_oo = []
    for j in range(int(b)):
        copy_oo.append(int(one[i][j]) * int(two[i][j]))
    oo.append(copy_oo)
print(oo)
    

