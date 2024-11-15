import math

def sft(num_arr, power):
    #  mult by power of ten. In other words, shift the dot to the left
    return num_arr + [0] * power


def normalize_shape(x, y):
    dif  = len(x) - len(y)

    if dif != 0:
        l = [0] * abs(dif)

        if dif > 0:
            y = l + y
        else:
            x = l + x

    return x, y




def ksum(x, y):
    x, y = normalize_shape(x, y)

    len_x = len(x)

    result = [0] * len_x
    carry = 0

    for i in range(len_x - 1, -1, -1):
        s = x[i] + y[i] + carry
        carry=0

        if s > 9:
            carry = math.floor(s / 10)
            s = s % 10

        result[i] = s

    if carry > 0:
        result = [carry] + result

    return result



def kmult(x, y):
    if len(x) != len(y):
        raise Exception("For a while, its restrict to n digits for x and y")

    n = len(x)
    n2 = math.ceil(n / 2)

    p, q = x[:n2], x[n2:]
    r, s = y[:n2], y[n2:]

    #  print_data(x, y, n, p, q, r, s)

    if n == 1:
        p = x[0] * y[0]
        if p > 10:
            unity   = p % 10
            decimal = math.floor(p / 10)
            p = [decimal, unity]
        else:
            p = [p]

        return p

    pr = kmult(p, r)
    ps = kmult(p, s)
    qr = kmult(q, r)
    qs = kmult(q, s)

    product = ksum(ksum(sft(pr, n), sft(ksum(ps, qr), n2)), qs)

    return product



def print_data(x, y, n, p, q, r, s):
    print("\nData:")
    print("x: " + str(x))
    print("y: " + str(y))
    print("n: " + str(n))
    print("p: " + str(p))
    print("q: " + str(q))
    print("r: " + str(r))
    print("s: " + str(s))


def test(x, y, r):
    return kmult(x, y) == r


def main():
    print(test([2], [6], [1, 2]))
    print(test([2, 3], [6, 7], [1, 5, 4, 1]))
    print(test([0, 0, 2, 3], [0, 1, 6, 7], [0, 0, 0, 3, 8, 4, 1]))
    print(test([0, 0, 2, 3], [0, 0, 6, 7], [0, 0, 0, 1, 5, 4, 1]))
    print(test([1, 2, 3, 4], [6, 7, 8, 9], [8, 3, 7, 7, 6, 2, 6]))
    print(test([0, 7, 8, 9], [0, 5, 6, 7], [0, 4, 4, 7, 3, 6, 3]))
    print(test([8, 9, 7, 0], [7, 3, 9, 0], [6, 6, 2, 8, 8, 3, 0, 0]))
    print(test([1, 2, 3, 4, 1,2 ,3, 4], [6, 7, 8, 9, 6, 7, 8,9 ], [8, 3, 7, 9, 3, 0, 1, 6, 0, 8, 9, 7, 6, 2, 6]))
   
   #  dar reshape no kmult e evitar exception;
   #  dar reshape no kmult e evitar exception;
   #  dar reshape no kmult e evitar exception;

    #  remover os zeros a esquerda do resultado
    #  remover os zeros a esquerda do resultado
    #  remover os zeros a esquerda do resultado

if __name__ == "__main__":
    main()

