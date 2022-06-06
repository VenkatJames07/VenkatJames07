def check(lg):
    flag = 0
    for i in lg.keys():
        if lg[lg[i]] < lg[i]:
            lg[i] = lg[lg[i]]
            flag += 1
    if flag == 0:
        return 0
    else:
        check(lg)


s1 = input()
s2 = input()
s3 = input()
lg = {}
for i in range(97, 123):
    lg[chr(i)] = chr(i)

for i in range(len(s1)):
    if (s1[i] < s2[i]):
        lg[s2[i]] = s1[i]
    elif (s1[i] > s2[i]):
        lg[s1[i]] = s2[i]
    check(lg)

res = ""
for i in range(len(s3)):
    res += lg[s3[i]]
print(res)

