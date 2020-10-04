# find out occurrences of all the words, print the maximum occurrences word:
#
# words = ["mkdir","echo","mkdir","echo","mkdir","cat","lsmod","cat"]
# o/p = {"cat":2,"echo":2,"mkdir":3,"lsmod":1},
#            print -->"mkdir"

words = input()
words = words.split()
dictionary = dict()
values = 0

for i in words:
    if i in dictionary.keys():
        dictionary[i] = dictionary[i] + 1
        if dictionary[i] > values:
            values = dictionary[i]
    else:
        dictionary[i] = 1
print(dictionary)

for key,val in dictionary.items():
    if val == values:
        print(key,val)

# occurrence = dict()
#
# for word in words:
#     if occurrence.get(word):
#         occurrence[word] = occurrence[word] + 1
#     else:
#         occurrence[word] = 1
#
# print(occurrence)
#
# Max = max(list(occurrence.values()))
#
# for key,val in occurrence.items():
#     if Max == val:
#         print(key)

# maximumoccurrence = max(occurrence,key=occurrence.get)
# print(occurrence.get())
# print(maximumoccurrence)