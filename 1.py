num_in = input("請輸入正整數:")
num = []
biggest = 0
for i in range(0,len(num_in)):
    for j in range(0,len(num_in)):
        if num_in[i:j+1] != '' and num_in[i:j+1] != num_in:
            num.append(num_in[i:j+1])
for i in range(0,len(num)):    
    TorF = True
    for j in range(2,int(num[i])):
        if int(num[i]) % j == 0:
            TorF = False
            break
    if TorF == True and int(num[i]) > biggest:
        biggest = int(num[i])
if biggest == 0:
    print("No Prime found")
else:
    print(biggest)



