n = int(input())
P_list = list(map(int,(input().split(" "))))
#print(P_list)
count = 0
i = 0
for i in range(n-2):
    if P_list[i] > P_list[i+1] > P_list[i+2] or P_list[i] < P_list[i+1] < P_list[i+2]:
        count = count + 1


print(count)
