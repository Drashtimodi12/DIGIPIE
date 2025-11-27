# Dictionary task — Count frequency of characters in a string

def greet(fun):
    # Decorator function
    def start():
        print("-----START-----")

        # Take input from user and convert it to lowercase
        # lowercase makes counting easy (A and a become same)
        a = input("Enter string to check frequency: ").lower()

        fre = {}  # empty dictionary to store frequency counts

        # Loop through each character in the string
        for i in a:
            # If character already exists in dictionary, increase count
            if i in fre:
                fre[i] += 1
            else:
                # If character appears for the first time, set count = 1
                fre[i] = 1

        # Call the original function with the frequency dictionary
        fun(fre)

        print("-----END-----\n")
    return start


@greet
def st(fre):
    # This function prints the frequency dictionary
    print(fre)


st()

# OP:
# -----START-----
# Enter string to check frequency: daeasd
# {'d': 2, 'a': 2, 'e': 1, 's': 1}
# -----END-----

print("\n==================================\n")

def greet(fun):
    def start():
        print("-----START-----")
        a = [1, 4, 2, 5, 7, 4]
        fre = {}
        for i in a:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1
        fun(fre)
        print("-----END-----\n")
    return start

@greet 
def num(fre):
    print(fre)

num()

# OP:
# -----START-----
# {1: 1, 4: 2, 2: 1, 5: 1, 7: 1}
# -----END-----