def longestCommonPrefix(self, A):
    pre=''
    b=A[0]
    for a in A:
        b=self.check(b,a)
    return b

def check(self, b, a):
    c=''
    for i in range(0,min(len(b),len(a))):
        if b[i] == a[i]:
            c+=b[i]
    return c