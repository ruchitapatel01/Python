# Remove duplicates
# Challenge - Try to solve with strictly one for loop iteration, i.e. no nested loops should be used
# k = [15,12,13,15,23,15]

arr = list(map(int, input().split()))
non_duplicate = []

for i in arr:
    if i not in non_duplicate:
        non_duplicate.append(i)

print(non_duplicate)