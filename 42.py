a = int(input())
b = int(input())
c = int(input())
ans = []
if b**2 - 4*a*c < 0:
    ans.append(0)
elif b**2 - 4*a*c == 0:
    ans.append(-b/(2*a))
else:
    ans.append((-b+((b**2 - 4*a*c)**0.5))/2*a)
    ans.append((-b-((b**2 - 4*a*c)**0.5))/2*a)
if len(ans) == 1:
    print(ans[0])
else:
    print(ans[0])
    print(ans[1])








# def compute(a,b,c):
#     q=b**2-4*a*c
    
#     if q<0:
#         output="Your equation has no root."
#     elif q==0:
#         output=-b/2*a
#     else:
#         q1=(-b+q**0.5)/(2*a)
#         q2=(-b-q**0.5)/(2*a)
#         output='{}, {}'.format(q1, q2)
#     return output
        

# a=eval(input())
# b=eval(input())
# c=eval(input())
# print(compute(a,b,c))