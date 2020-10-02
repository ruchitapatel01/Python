# Finding unique elements from array (in sorted order)
#
# arr = [23,45,78,9,2,-1,-23,23,45,67,78,9,22,2]
# Ans = [-23,-1,2,9,22,23,45,67,78]

arr = list(map(int, input().split()))
dictionary = dict()
result = []

for i in arr:
    if i in dictionary.keys():
        dictionary[i] = dictionary[i] + 1
    else:
        dictionary[i] = 1

for i in sorted(dictionary):
    result.append(i)

print(result)