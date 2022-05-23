while True:
    time = 0
    text = input("檢測的字串(end結束):")
    if text == "end":
        print("檢測結束")
        break
    else:
        tt = input("檢測的單一字元:")
        for i in text:
            if tt == i:
                time += 1
        print("字元"+tt+"出現次數為:"+str(time))
    