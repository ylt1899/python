num1 = []
num2 = []
out = []
a = []
for o in range(0,2):
    inp0 = input().split(" ")
    num = []
    out = []
    for i in range(0,int(inp0[0])):
        for j in range(0,int(inp0[1])):
            a.append(0)
        num.append(a)
        out.append(a)
        a = []
    for i in range(0,int(inp0[0])):
        inp1 = input().split(" ")
        for j in range(0,len(inp1)):
            num[i][j] = inp1[j]
    if o == 0:
        num1 = num
    else:
        num2 = num
for i in range(0,int(inp0[0])):
    for j in range(0,int(inp0[1])):
        out[i][j] = int(num1[i][j]) + int(num2[i][j])
print(out)
