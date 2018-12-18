import itertools, copy
class Solution:
    def combine(self, n, r):
        iterable=[]
        for i in range(1, n+1):
            iterable.append(i)
        pool = list(iterable)
        if r > n:
            return
        indices = list(range(r))
        yield list(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield list(pool[i] for i in indices)


s=Solution()
print(list(s.combine(4,2)))