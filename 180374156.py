def function(x):
    return (x-60.1234535678)*(x-60.1234535678)


def six18(f, a, b):
    e = 0.000001
    r = 0.618
    b1 = a + r*(b-a)
    a1 = b - r*(b-a)
    if b - a < e:
        print((a+b)/2)
    elif a1 < b1:
        print((a+b1)/2)
        six18(function, a, b1)
    elif a1 > b1:
        print((a1+b)/2)
        six18(function, a1, b)
    else:
        print((a1+b1)/2)    # 最低点在两值中间


if __name__ == "__main__":
    six18(function, 31, 90)
