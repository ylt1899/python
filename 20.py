from copy import copy


time = int(input("組數為:"))
copy1 = []
text = []
for i in range(time):
    copy1 = input("第"+str(i+1)+"組為:").split(" ")
    text.append("第"+str(i+1)+"組應收費用:"+str(250*int(copy1[0])+175*int(copy1[1])))
for i in range(time):
    print(text[i])