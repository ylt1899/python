from sqlalchemy import true
while(true):
    inp1 = input().split(" ")
    inp2 = input().split(" ")
    inp3 = input().split(" ")
    if inp3 == "-1":
        break
    same = 0
    same1 = 0 #計算 同花色的排有幾張
    same2 = 0
    #第一副牌 有幾張一樣的花色
    for i in range(0,len(inp1)):
        for j in range(0,len(inp1)):
            if inp1[i][0] == inp1[j][0]:
                same += 1
            if same > same1:
                same1 = same
        same = 0
    #第二副牌 有幾張一樣的花色
    for i in range(0,len(inp2)):
        for j in range(0,len(inp2)):
            if inp2[i][0] == inp2[j][0]:
                same += 1
            if same > same2:
                same2 = same
        same = 0
    if same1 > same2:
        print(1)
    elif same2 > same1:
        print(0)
    

