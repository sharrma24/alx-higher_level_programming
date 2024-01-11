#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    from calculator_1 import add, sub, mul, div

    sum_result = add(a, b)
    diff_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print("{} + {} = {}".format(a, b, sum_result))
    print("{} - {} = {}".format(a, b, diff_result))
    print("{} * {} = {}".format(a, b, mul_result))
    print("{} / {} = {}".format(a, b, div_result))
