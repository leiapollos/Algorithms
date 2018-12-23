def reverseWords(A):
    s=''
    ss=[]
    for a in A:
        if a != ' ':
            s+=a
            continue
        ss.append(s)
        s=''
    ss.append(s)
    s=''
    for i in range(1, len(ss)+1):
        if i==1:
            s+=ss[-i]
            continue
        s+=' '
        s+=ss[-i]
    return s

A = "fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq"
print(reverseWords(A))