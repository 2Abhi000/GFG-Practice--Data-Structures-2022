#Farthest number
def farthest_min(a, n):
    suffix_min = [0 for i in range(n)]
    suffix_min[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], a[i])
    for i in range(n):
        low = i + 1
        high = n - 1
        ans = -1
        while (low <= high):
            mid = (low + high) // 2
            if (suffix_min[mid] < a[i]):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        print(ans, end=" ")
ar=[]
n = int(input("Size: "))
for i in range(n):
    ar.append(int(input("Value: ")))
ans=farthest_min(ar,n)