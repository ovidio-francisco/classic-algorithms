#!/usr/bin/env python3


def merge(a, b):
    result = []

    while (len(a) > 0 and len(b) > 0):
        min_a = min(a)
        min_b = min(b)

        if min_a < min_b:
            result = result + [min_a]
            a.remove(min_a)
        else:
            result = result + [min_b]
            b.remove(min_b)

    remaining = a if len(a) > 0 else b
    result = result + merge_sort(remaining)

    return result



def merge_sort(a):

    if (len(a) < 2):
        return a

    mid = len(a) // 2

    l = a[:mid]
    r = a[mid:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)



def main():
    print("--- Merge Sort ---\n")
    print(merge_sort([3, 4, 5, 3, 5, 1, 8, 5, 2]))
    print(merge_sort([3, 4, 5, 3, 5, 8, 5, 2]))


if __name__ == "__main__":
    main()


#  https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/
