n = int(input("輸入值n為:"))
s = 0
dx = 1
for i in range(0,n*100,dx):
    i = i / 100
    s = s +((i*i+1)*(dx/100))
print(f"{s:.1f}")