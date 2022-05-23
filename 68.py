num_a = list(input("請輸入第一組數字:"))
num_b = list(input("請輸入第二組數字:"))
A,B = 0,0
for i in range(len(num_a)):
    if num_a[i] in num_b and num_a[i] == num_b[i]:
        A += 1
    elif num_a[i] in num_b and num_a[i] != num_b[i]:
        B += 1
if A == len(num_a):
    print(f"{A}A{B}B 全對")
else:
    print(f"{A}A{B}B 加油")


