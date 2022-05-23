test,student = input("請輸入考試次數及學生數:").split(" ")
pp = input("每次考試所佔的比率:").split(" ")
student_score = []
total = 0
for i in range(int(student)):
    score = input().split(" ")
    student_score.append(score)
print(student_score)
for i in range(int(student)):
    for j in range(int(test)):
        total += int(student_score[i][j]) * float(pp[j])
print(f"全班的總平均值為:{total/3:.2f}")




