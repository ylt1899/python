text = [["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
t = input("輸入查詢學號為:")
for i in range(len(text)):
    if t == text[i][0]:
        print(text[i][0]+" "+text[i][1]+" "+text[i][2])