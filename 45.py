dic = {0:"普通",1:"吉",2:"大吉"}
M = int(input())
D = int(input())
S = (M*2+D)%3
print(dic[S])