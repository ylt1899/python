M = int(input("請輸入階乘值:"))
ans = 1
n = 0
while(ans < M):
    n += 1
    ans *= n
print("超過M為"+str(M)+ "的最小階乘N值為:"+str(n)) 