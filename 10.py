from matplotlib.pyplot import text
from sympy import false, true
out = false
list_all = []
list_out = []
list_num = []
while(out == false):
    text0 = input("輸入N及M為:")
    if text0 == "0":
        print("結束")
        break
    else:
        N,M = text0.split(" ")
        for i in range(int(N)):
            list_all.append(input("輸入矩陣值第"+str(i+1)+"列為:").split(" "))
    # print(list_all)
        for i in range(int(M)):
            for j in range(int(N)):
                list_num.append(list_all[j][i])
            list_out.append(list_num)
            list_num = []
            print("輸出矩陣數值第"+str(i+1)+"列為:" +list_out[i][0] + " "+list_out[i][1])

