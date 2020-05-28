t = int(input())

while t > 0:
    n1, n2 = list(map(int, input().split()))
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    i, j, newA = 0, 0, []
    while i < n1 and j < n2:
        if a1[i] < a2[j]:
            newA.append(a1[i])
            i += 1
        elif a2[j] < a1[i]:
            newA.append(a2[j])
            j += 1
        else:
            newA.append(a1[i])
            newA.append(a2[j])
            i += 1
            j += 1

    while i < n1:
        newA.append(a1[i])
        i += 1

    while j < n2:
        newA.append(a2[j])
        j += 1

    print(" ".join(map(str, newA)))

    t -= 1
