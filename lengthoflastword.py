def lengthOfLastWord(A):
    s=''
    i=1
    l = len(A)
    while(A[-i]==' '):
        i+=1
    for j in range(i, len(A)+1):
        if A[-j] != ' ':
            s+=A[-j]
            continue
        break
    return len(s)

A = 'asf  hvdsfjhwnjh ksjdbiwbfs dsdggd  '
print(lengthOfLastWord(A))