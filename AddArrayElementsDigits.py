arr = list(map(int, input().split()))
add = 0

for x in arr:
    x = str(x)
    for i in x:
        add = add + int(i);

print(add)