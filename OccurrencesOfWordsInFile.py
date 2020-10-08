# a text file is given with 10 lines
# read that file
# find occurrences of all the possible words

file = open("TextFile.txt")
dictionary = dict()
result = []

for line in file:
    for words in line.split():
        if words in dictionary.keys():
            dictionary[words] = dictionary[words] + 1
        else:
            dictionary[words] = 1

for key,val in dictionary.items():
    if val == 1:
        result.append(key)

file.close()

file = open("TextFile.txt","a")
file.write("\n" + str(result)),
file.close()

# for key,val in dictionary.items():
#     if val == values:
#         print(key,val)