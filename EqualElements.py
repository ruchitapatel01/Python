# A=[10,10,10,10], decide whether all elements are equal

A = [10,10,11,10]
T = ("A","A","A")
temp = A[0]
count = 0

for i in A:
    if temp == i:
        count = 0
    else:
        count= 1
        break

if count == 0:
    print("All Elements are same")
else:
    print("All Elements are not same")