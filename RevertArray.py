# given array = [1,2,3,4,5], revert it without using any library functions.

a = [1,2,3,4,5]
count = 0

for i in a:
    count+=1

i=0
j=count-1
while i<j:
    a[i],a[j] = a[j],a[i]
    i+=1
    j-=1

print(a)