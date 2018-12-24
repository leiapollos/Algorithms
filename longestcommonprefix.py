def longestCommonPrefix(A):
    pre=''
    b=A[0]
    for a in A:
        b=check(b,a)
    return b

def check(b, a):
    c=''
    for i in range(0,min(len(b),len(a))):
        if b[i] == a[i]:
            c+=b[i]
    return c