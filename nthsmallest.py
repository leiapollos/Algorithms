def swap(arr, a, b): 
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x: 
            swap(arr, i, j)
            i+=1
    swap(arr, i, r)
    return i

def nthsmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        pos = partition(arr, l, r)

        if pos-l == k-1: 
            return arr[pos] 
        if pos-l > k-1:
            return nthsmallest(arr, l, pos-1, k)

        return nthsmallest(arr, pos+1, r, k-pos+l-1) 

    return max(arr)


arr = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
k = 9
n = int(len(arr))
print(nthsmallest(arr, 0, n-1, k))