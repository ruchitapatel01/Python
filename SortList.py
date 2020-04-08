# L=[23,45,66,77,22,21,24,22], sort it in descending order. No lib should be used.

L=[23,45,66,77,22,21,24,22]

for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        if L[i]<L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

print(L)