def outer():
    y = 20

    def inner():
        print(y)  # enclosed variable

    inner()

outer()
