text1,text2 = "紅豆生南國,春來發幾枝?願君多采擷,此物最相思。","春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少。"
thesame = []
for i in text1:
    if i != "," and i != "。" and i in text2 and i not in thesame:
        thesame.append(i)
print(thesame)