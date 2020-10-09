# a text file is given with 10 lines
# read that file
# find occurrences of all the possible words
# Modify ur unique words code for 100 files
# For those 100 files I want all unique words stored into same files.

import os
import re

for file_name in os.listdir("text_file_bunch"):
    file = open("text_file_bunch\\" + file_name)
    dictionary = dict()
    result = []

    for line in file:
        for words in line.split():
            words = re.sub('[^A-Za-z0-9]+', '', words)
            if words in dictionary.keys():
                dictionary[words] = dictionary[words] + 1
            else:
                dictionary[words] = 1

    for key,val in dictionary.items():
        result.append(key)
    file.close()

    file = open("text_file_bunch\\" + file_name,"a")
    file.write("\n" + str(result)),
    file.close()