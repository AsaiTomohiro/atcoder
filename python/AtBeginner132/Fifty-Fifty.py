#４文字の文字列Sが二種類で2回ずつ現れる判定
S = input()
S_list = set(list(S))
#print(S_list)




if len(S_list) == 2:
    print("Yes")
else:
    print("No")
