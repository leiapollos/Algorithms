import itertools, copy
def subsets(A):
    l=[]
    A.sort()
    for i in range(1, len(A)+1):
        temp = itertools.combinations(A, i)
        temp2 = []
        for elem in temp:
            temp2.append(list(elem))
        l+=temp2
        l.sort()
    return [[]]+l


print(subsets([ 15, 20, 12, 19, 4 ]))