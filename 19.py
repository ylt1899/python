from copy import copy
from errno import ESTALE


time = int(input("測試的資料量:"))
copy1 = []
data = []
for i in range(time):
    copy1 = input().split(" ")
    data.append(copy1)
for i in range(time):
    if data[i][0] == "O" and data[i][1] == "O":
        if data[i][2] == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif data[i][0] == "O" and data[i][1] == "A" or data[i][0] == "A" and data[i][1] == "O":
        if data[i][2] == "A" or data[i][2] == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif data[i][0] == "O" and data[i][1] == "B" or data[i][0] == "B" and data[i][1] == "O":
        if data[i][2] == "B" or data[i][2] == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif data[i][0] == "O" and data[i][1] == "AB" or data[i][0] == "AB" and data[i][1] == "O":
        if data[i][2] == "A" or data[i][2] == "B":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif data[i][0] == "A" and data[i][1] == "A":
        if data[i][2] == "A" or data[i][2] == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif data[i][0] == "A" and data[i][1] == "B" or data[i][0] == "B" and data[i][1] == "A":
        print("YES")
    elif data[i][0] == "A" and data[i][1] == "AB" or data[i][0] == "AB" and data[i][1] == "A":
        if data[i][2] == "O":
            print("IMPOSSIBLE")
        else:
            print("YES")
    elif data[i][0] == "B" and data[i][1] == "B":
        if data[i][2] == "B" or data[i][2] == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif data[i][0] == "B" and data[i][1] == "AB" or data[i][0] == "AB" and data[i][1] == "B":
        if data[i][2] == "O":
            print("IMPOSSIBLE")
        else:
            print("YES")
    elif data[i][0] == "AB" and data[i][1] == "AB":
        if data[i][2] == "O":
            print("IMPOSSIBLE")
        else:
            print("YES")