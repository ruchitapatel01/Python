# T=("A","B","C") , Q=("D","E","F"), generate S=("AD","BE","CF") tupple.

# def add(T,Q):
#     str = T.join(Q)
#     return str

T=("A","B","C")
Q=("D","E","F")
tp = ()

for i in range(len(T)):
    str = T[i] + Q[i]
    tp = tp + (str,)

print(tp)