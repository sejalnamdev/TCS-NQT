n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

mn = min(arr)
mx = max(arr)

mini = arr.index(mn)
maxi = arr.index(mx)

left = max(mini, maxi) + 1
right = n - min(mini, maxi)
both = (min(mini, maxi) + 1) + (n - max(mini, maxi))

print(min(min(left, right), both))