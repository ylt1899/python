num = input().split(",")
same,time = 0,0
for i in range(len(num)):
    for j in range(len(num)):
        if num[i] != num[j]:
            if int(num[i]) < int(num[j]):
                time = int(num[i])
            else:
                time = int(num[j])
            for k in range(1,time+1):
                if int(num[i]) % k == 0 and int(num[j]) % k == 0 and k > same:
                    same = k
print(same)