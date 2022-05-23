book_A = ["飢餓遊戲3","解憂雜貨店","怪獸與牠們的產地","哈利波特6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"]
book_B = ["房思琪的初戀樂園","等一個人咖啡","鬼滅之刃14","神農嘗百草","麥田捕手","老人與海","傲慢與偏見","與神同行"]
find = input("請輸入欲租借的書籍:")
if find in book_A:
    for i in range(len(book_A)):
        if find == book_A[i]:
            print("在書架A的第%d本"%(i+1))
elif find in book_B:
    for i in range(len(book_B)):
        if find == book_B[i]:
            print("在書架B的第%d本"%(i+1))
else:
    print("查無此書籍")