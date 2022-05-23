time = int(input())
text,oo,oo_text = [],[],[]
for i in range(time):
    text,tt = [],0
    for j in range(4):
        text.append(int(input()))
    for k in range(3):
        if text[k] + 1 == text[k+1]:
            tt += 1
            if tt == 3:
                text.append(text[3]+1)
                oo_text.append("此為等差數列")
        elif text[k] * 2 == text[k+1]:
            tt += 1
            if tt == 3:
                text.append(text[3]*2)
                oo_text.append("此為等比數列")
        else:
            oo_text.append("都不是")
    oo.append(text)
for i in range(time):
    print(oo[i])
    print(oo_text[i])

