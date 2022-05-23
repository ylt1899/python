text = [["123","456","9000"],["456","789","5000"],["789","888","6000"],["336","558","10000"],["775","666","12000"],["566","221","7000"]]
cash = []
time = int(input("輸入查詢組數:"))
for i in range(time):
    t = input().split(" ")
    a = 0
    for i in range(len(text)):
        if t[0] == text[i][0] and t[1] == text[i][1]:
            a = 1
            cash.append(text[i][2])
            break
    if a == 0:
        cash.append("error")
for i in cash:
    print(i)
        