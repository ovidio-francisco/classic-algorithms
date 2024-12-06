
def kadane(a):
    cur = a[0]
    glo = a[0]

    for e in a[1:]:
        cur = max(e, cur + e)
        glo = max(cur, glo)

    return glo
