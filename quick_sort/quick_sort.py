


def quick_sort(a):
    pivot = len(a) // 2
    print("a: " + str(a))
    print("p: " + str(a[pivot]))

    if len(a) < 2:
        return

    l = []
    r = []

    for i in range(len(a)):
        if a[i] <= a[pivot]:
            l.append(a[i])
        else:
            r.append(a[i])

    print("l: " + str(l))
    print("r: " + str(r))

    quick_sort(l)
    quick_sort(r)


a = [2, 8, 4, 2, 7, 9, 4, 2, 1, 6, 0, 3, 5, 7]
quick_sort(a)

