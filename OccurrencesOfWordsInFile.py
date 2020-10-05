# a text file is given with 10 lines
# read that file
# find occurrences of all the possible words

file = open("TextFile.txt")
dictionary = dict()
values = 0

for line in file:
    for words in line.split():
        if words in dictionary.keys():
            dictionary[words] = dictionary[words] + 1
            if dictionary[words] > values:
                values = dictionary[words]
        else:
            dictionary[words] = 1
file.close()

file = open("TextFile.txt","a")
file.write("\n" + str(dictionary))
print(dictionary)
file.close()

# for key,val in dictionary.items():
#     if val == values:
#         print(key,val)