inp = input("輸入一組四位數為:")
list_inp = list(inp)
num = 0
out = ""
for i in range(0,len(list_inp)):
    list_inp[i] = (int(list_inp[i]) + 7)%10
# 交換位置
num = list_inp[0]
list_inp[0] = list_inp[2]
list_inp[2] = num
num = list_inp[1]
list_inp[1] = list_inp[3]
list_inp[3] = num
for i in range(0,len(list_inp)):
    out += str(list_inp[i])
print("輸出加密後的數字為:" + out)


