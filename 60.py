ee = ["a","e","i","o","u"]
text_in = list(input("輸入一串小寫英文:"))
text = ""
for i in range(len(text_in)):
    if text_in[i] in ee:
        text_in[i] = "."
    text += text_in[i]
print(text)