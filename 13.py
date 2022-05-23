list_word = list(input("輸入一字元為:"))
list_word2 = list_word.copy()
list_word2.reverse()
if list_word == list_word2:
    print("Yes")
else:
    print("No")