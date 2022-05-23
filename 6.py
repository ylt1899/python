list_num = input("輸入值:").split(",")
list_num.sort()
list_num1 = list_num.copy()
small = list_num
list_num1.reverse()
big = list_num1
num_min = ""
num_max = ""
for i in range(len(list_num)):
    num_max += big[i]
    num_min += small[i]
print(str(int(num_max)-int(num_min)))

