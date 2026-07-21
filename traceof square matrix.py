n = int(input())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

sum = 0

for i in range(n):
    for j in range(n):
        if i == j:
            sum += arr[i][j]

print(sum)
