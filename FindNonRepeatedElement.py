# given an array InArr = [1,1,2,2,3,4,4,5,5], find the non-repeated element.

arr = list(map(int, input().split()))

for i in range(len(arr)):
    j = 0
    while(j<len(arr)):
        if arr[i] == arr[j] and i != j:
            break
        j = j + 1
    if(j == len(arr)):
        print(arr[i])

