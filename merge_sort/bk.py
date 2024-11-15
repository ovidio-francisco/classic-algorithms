#!/usr/bin/env python3

#  Merge Step:

    #  Merge the two sorted halves into a single sorted list by:
        #  Comparing the smallest unmerged elements from each half.
        #  Adding the smaller element to the result list.
        #  Repeat until all elements are merged.


def merge(a, l, m, r):
    return a



def merge_sort(a, l, r):
    print("")
    print("a = " + str(a[l:r]))
    print("l = " + str(l))
    print("r = " + str(r))

    input("continue: ")

    if ((r - l) < 2):
        print('returning = ' + str(a[l]))
        return a

    mid = (l + r) // 2
    print("mid = " + str(mid))

    merge_sort(a, l, mid)
    merge_sort(a, mid + 1, r)




def main():
    a = [3, 4, 5, 3, 5, 8, 5, 2]
    merge_sort(a, 0, len(a))
    print("--- Merge Sort ---")


if __name__ == "__main__":
    main()


#  https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/
