# L =['jdkd','dsdjakj','dskdhid',78,95,344]. reverse all elements of this list

L =['jdkd','dsdjakj','dskdhid',78,95,344]
M = []

for i in L:
    if isinstance(i,str) == True:
        i = i[::-1]
        M.append(i)
    else:
        rev = 0
        while (i > 0):
            rem = i % 10
            rev = (rev * 10) + rem
            i = i // 10
        M.append(rev)

print(M)