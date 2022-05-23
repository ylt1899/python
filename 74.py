answer = ["red","blue","red","green"]
text = input().split(" ")
text_out = ""
for i in range(len(text)):
    if text[i] == answer[i]:
        text_out += "1"
    elif text[i] in answer and text[i] != answer[i]:
        text_out += "2"
    else:
        text_out += "3"
if text_out == "1111":
    print("正確答案")
else:
    print(text_out)