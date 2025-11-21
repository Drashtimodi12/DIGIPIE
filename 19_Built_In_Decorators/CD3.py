# Task 14: Create a class Library with: 
# list of books # methods: 
# add_book() 
# remove_book()
# display_books() 
# search_book() 
# Test using different objects.


class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter Book name to add in School Bag: ").strip().title()
        self.books.append(book)
        print(f"'{book}' has been added to the School Bag.")

    def remove_book(self):
        book = input("\nEnter Book name to remove from School Bag: ").strip().title()
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' has been removed from the School Bag.")
        else:
            print(f"'{book}' not found in the School Bag.")

    def display_books(self):
        if len(self.books) == 0:
            print("\nSchool Bag is empty.")
        else:
            print("\nBooks in School Bag:")
            for b in self.books:
                print("-", b)

    def search_book(self):
        book = input("\nEnter Book name to search in School Bag: ").strip().title()
        if book in self.books:
            print(f"'{book}' is present in the School Bag.")
        else:
            print(f"'{book}' is NOT present in the School Bag.")


l = Library()

l.add_book()
l.add_book()
l.add_book()

l.display_books()
l.remove_book()
l.search_book()
