time1 = input("請輸入時間1(時:分:秒):").split(":")
second = int(time1[0])*3600 + int(time1[1])*60 + int(time1[2])
time2 = int(input("請輸入時間2(秒):"))
time2_min,time2_sec,time2_ms = 0,0,0
time2_min = int(time2/3600)
time2_sec = int((time2-(time2_min*3600))/60)
time2_ms = time2-(time2_min*3600)-(time2_sec*60)
print(f"時間1({time1[0]}:{time1[1]}:{time1[2]})格式轉換後為{second}秒")
print(f"時間2({time2}秒)={time2_min}:{time2_sec}:{time2_ms}")

