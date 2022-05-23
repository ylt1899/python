dict_text,oo = {},[]
text = list(input())
for i in text:
    if i != "," and i != "。" and i not in dict_text:
        dict_text.update({i:1})
    elif i != "," and i != "。" and i in dict_text:
        dict_text[i] += 1
for i in dict_text:
    if dict_text[i] > 1:
        oo.append(i)
print(oo)
