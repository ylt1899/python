dic = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
text = input().split(" ")
num = 0
for i in range(5):
    num += dic[text[i]]
print(num)



