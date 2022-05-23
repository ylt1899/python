same,ll = 0,0
A = input("請輸入A的好友:").split(" ")
B = input("請輸入B的好友:").split(" ")
if A > B:
    ll = len(B)
else:
    ll = len(A)
for i in range(ll):
    if A[i] in B:
        same += 1
print(same)
