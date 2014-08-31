def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        recurse = fibonacci(n-1)
        recurse2 = fibonacci(n-2)
        result = recurse + recurse2
        return result


"""for i in range(10):
    print(fibonacci(i))
    """


