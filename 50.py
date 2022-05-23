all = ["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"]
english_pass = ["John","Mary","Fiona","Claire","Ben","Bill"]
math_pass = ["Mary","Fiona","Claire","Eva","Ben"]
all_pass,math_no_pass,one_pass = [],[],[]
for i in range(len(all)):
    if all[i] in math_pass and all[i] in english_pass:
        all_pass.append(all[i])
    if all[i] not in math_pass:
        math_no_pass.append(all[i])
    if all[i] in english_pass and all[i] not in math_pass:
        one_pass.append(all[i])
print("英文與數學都及格 "+ str(all_pass))
print("數學不及格 "+ str(math_no_pass))
print("英文及格且數學不及格 "+ str(one_pass))