# M=[(2,3),(3,2),(3,2),(2,3)] find out whether all tuple's element sum is equal or not. i.e (2,3) so 2+3 = 5. (3,2) so 3+2=5. So 5==5.

M=[(2,3),(3,2),(3,2),(2,3)]
add = sum(list(M[0]))
count = 0

for i in M:
    if add == sum(list(i)):
        add = sum(list(i))
        count = 0
    else:
        count+=1
        break

if count == 0:
    print("Tuple's element sum is equal")
else:
    print("Tuple's element sum is not equal")