# Create a custom iterator class that returns even numbers between 1 and 20.

class EvenNumbers:
    def __init__(self):
        self.n = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= 20:
            raise StopIteration
        x = self.n
        self.n += 2
        return x

for i in EvenNumbers():
    print(i)    


"""
ADVANCED LEVEL

Create a custom iterator class that returns even numbers from 1 to 20.

Create a custom iterator class that returns characters of a string one by one.

Create a generator function that yields squares of numbers up to n.

Create a generator that yields numbers divisible by 5 up to 100.

Create a generator that yields infinite natural numbers (stop after 10 calls).

Iterate using a generator expression (not list comprehension).

Use itertools.cycle() (if allowed) to repeat list elements (or write your own version).

Create a generator that reads a file line by line.

Create a custom iterator that counts down from 10 to 1.

Create a generator that yields Fibonacci numbers up to n terms.
"""