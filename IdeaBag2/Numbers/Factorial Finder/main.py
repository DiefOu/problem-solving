def find_factorial_loop(x):
    if x == 0:
        return 1
    else:
        out = 1
        for i in range(1, x + 1):
            out *= i
    return out


def find_factorial_recursion(x):
    if x == 0:
        return 1
    else:
        return find_factorial_step(x, 0)


def find_factorial_step(x, curr):
    if x == 1:
        return 1
    else:
        curr += x * find_factorial_step(x - 1, curr)
    return curr

a = int(input("Give number pls: "))
print("{}! is {} using loop method and {} using recursion method".format(a, find_factorial_loop(a),
                                                                         find_factorial_recursion(a)))
