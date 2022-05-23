dic = {"-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9"}
get = input().split(" ")
text_out = ""
for i in get:
    text_out += dic[i]
print(text_out)
# get = list(input())
# text_out = ""
# time = int(len(get)/5) 
# for i in range(0,time):
#     time2 = 5*(i+1)
#     text_copy = ""
#     for j in range(0+(5*i),time2):
#         text_copy += get[j]
#     text_out += dic[text_copy]
# print(text_out)


