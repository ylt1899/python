answer = input()
list_out = []
while True:
    a = 0
    b = 0
    text = input()
    if text == "0000":
        break
    for i in range(len(text)):
        if text[i] in answer and text[i] == answer[i]:
            a+=1
        elif text[i] in answer and text[i] != answer[i]:
            b+=1
    list_out.append("%dA%dB"%(a,b))
for i in range(len(list_out)):
    print(list_out[i])