def demo():
    try:
        a = int(input("Enter integer number: "))
        print("You enter: ", a)
    except Exception as e:
        print(e)
    finally:
        print("Finally Block Executed. ")

d = demo()
