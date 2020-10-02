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

for key,val in dictionary.items():
    if val == values:
        print(key,val)