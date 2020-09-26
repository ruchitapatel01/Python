# find out a non-repeated character in a array of strings S={'fdaosdaos','gfdgrr','iooqqwessewfi'}

string = input()
arr = string.split()
res = []

for i in arr:
    j = list(i)
    repeated = []
    non_repeated = []
    for k in j:
        if k not in non_repeated:
            non_repeated.append(k)
        else:
            repeated.append(k)
    res.append(list(set(j).difference(repeated)))
for c in range(1,len(res)):
    if res[c] != res[0]:
        res = []
        break
    else:
        res.remove(res[c])

print(res)




