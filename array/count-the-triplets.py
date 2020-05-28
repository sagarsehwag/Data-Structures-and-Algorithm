t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)

    count = 0
    countState = {}

    for i in range(n-1):
        for j in range(i+1, n):
            sum = a[i] + a[j]
            if sum in s:
                count += 1

    if count == 0:
        print(-1)
    else:
        print(count)
