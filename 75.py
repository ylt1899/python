from sqlalchemy import true


work = []
while true:
    write = input("請輸入事項(若已無事項,請輸入end):")
    if write == "end":
        break
    work.append(write)
for i in range(len(work)):
    print(f"{i+1}. {work[i]}")