# W = [32,32,32,32,32,33,55,55,33,32,55] , get maximum numbers of occurrence list. i.e. [32,32,32,32,32,32]

def max(W):
    count = 0
    temp = W[0]
    for i in W:
        current = W.count(i)
        if current > count:
            count = current
            temp = i
    return temp

# W = [32,32,32,32,32,33,55,55,33,32,55]
# W = [22,32,32,32,32,32,33,55,55,33,32,55]
W =  [34,44,34,33,33,33,55,55,55,66]
ocr = max(W)
print([ocr] * W.count(ocr))