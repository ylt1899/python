dic = {"國文" : 0 ,"英文" : 0 ,"微積分" : 0 ,"體育" : 0 ,"程式設計" : 0}
dic["國文"] = int(input("國文:"))
dic["英文"] = int(input("英文:"))
dic["微積分"] = int(input("微積分:"))
dic["體育"] = int(input("體育:"))
dic["程式設計"] = int(input("程式設計:"))
score = (dic["國文"]+dic["英文"]+dic["微積分"]+dic["體育"]+dic["程式設計"])/5
print("平均分數:"+str(score))
print("最高分科目:"+max(dic,key=dic.get)+str(dic[max(dic,key=dic.get)])+"分")
print("最低分科目:"+min(dic,key=dic.get)+str(dic[min(dic,key=dic.get)])+"分")