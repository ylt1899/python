text_in = list(input("請輸入傳送密碼(6位數):"))
# i*4%7
text_out = ""
for i in range(len(text_in)):
    for j in range(1,10):
        if j*4%7 == int(text_in[i]):
            text_out += str(j)
            break
print(text_out)