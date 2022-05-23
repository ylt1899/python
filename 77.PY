f = open("data.txt","r",encoding="utf-8")
result = f.readlines()
record = []
blod_all = 0
blod_max = 0
blod_min = 1000
heart_all = 0
heart_max = 0
heart_min = 1000
for i in result:
    record.append(i.split("\n")[0].split(","))
for i in record:
    blod_all += float(i[0])
    if int(i[0]) > blod_max:
        blod_max = int(i[0])
    if int(i[0]) < blod_min:
        blod_min = int(i[0])
    heart_all += float(i[1])
    if int(i[1]) > heart_max:
        heart_max = int(i[1])
    if int(i[1]) < heart_min:
        heart_min = int(i[1])
print(f"血壓平均:{round(blod_all/len(record),2)}")
print(f"血壓最大值:{blod_max}")
print(f"血壓最小值:{blod_min}")
print(f"心跳平均:{round(heart_all/len(record),2)}")
print(f"心跳最大值:{heart_max}")
print(f"心跳最小值:{heart_min}")


