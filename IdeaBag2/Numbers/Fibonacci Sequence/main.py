def fibonacci_sequence(x):
    print ("1")
    if x != 1:
        print("1")
        a = 1
        b = 1
        for i in range(x - 2):
            print("{}".format(a + b))
            t = a + b
            a = b
            b = t

fibonacci_sequence(int(input("Enter number pls: ")))
