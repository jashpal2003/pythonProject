def expo(base,pow):

    if pow == 0:
        return 1
    print(base , pow)
    return base * expo(base,pow - 1)

print(expo(2,3))
