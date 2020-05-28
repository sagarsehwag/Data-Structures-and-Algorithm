t = int(input())

while t > 0:
    n = int(input())
    a = input().split()

    newA = []

    forwardPointer, reversePointer = 0, n-1
    while forwardPointer < reversePointer:
        newA.append(a[reversePointer])
        newA.append(a[forwardPointer])

        forwardPointer += 1
        reversePointer -= 1

    if forwardPointer == reversePointer:
        newA.append(a[forwardPointer])

    print(' '.join(newA))

    t -= 1
