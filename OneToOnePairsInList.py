# L = [1,2,3,4], M = [0,0,3,9]. Generate one to one pairs i.e. [(1,0),(2,0),(3,3),(4,9)]

L = [1,2,3,4]
M = [0,0,3,9]
N = []

output = [[L[a],M[b]] for a in range(len(L)) for b in range(len(M)) if a == b]

print(output)
