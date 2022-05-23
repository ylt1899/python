from sqlalchemy import true


n = int(input("請輸入n:"))
k = int(input("請輸入k:"))
total = 0
while true:
    if n < 1:
        break
    total += n
    n = n/k
print(f"Peter可以抽{int(total)}隻紙菸")