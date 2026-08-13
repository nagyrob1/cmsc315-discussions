"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Book:
    book_type = 'Paper Back'

    def __init__(self, title: str , author: str, pages: int):
        self.title = title
        self.author= author
        self.pages = pages

    def book_info(self):
        return f"title: {self.title} | Author {self.author} | page Number {self.pages}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Ebook(Book):

    device = 'Laptop'

    def __init__(self, title:str, author:str, pages: int, file_type: str, website: str, access_history: str):
        super().__init__(title, author, pages)


        self.file_type = file_type
        self.website = website


        if access_history is None:
            self.access_history = ["downloaded"]
        else:
            self.access_history= access_history

        def book_info(self):
            return f"Title: {self.title} | Author: {self.author} | page count: {self.pages} | File Type: {self.file_type} | website: {self.website}"


        def read_book(self):
            return f"you can read {self.title} on a {self.device}"




# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    ebook1 = Ebook("harry potter", "J.K Rowling", 320, "PDF", "books.com")
    ebook2 = Ebook("Lord of the Rings", "J.R.R. tolkien", 500, "word", "Goodbooks.com")

    print(f"Book accesses useing this device: {Ebook.device} ")
    print(f"ebook1 accesses via this device: {ebook1.device}")

    ebook1.bookmark = 75
    print(f"this is a bookmark i added to ebook1")

    print("ebook1 Instance Namespace: ")
    print(ebook1.__dict__)

    print("ebook2 isntanse namespace: ")
    print(ebook2.__dict__)

    print("Class namespace: ")
    print(list(ebook1.__dict__.keys()))

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():

    orignial = {
        "title": "python",
        "author": ['bob', 'jim'],
        "details": {
            'pages': 400,
            'genre': ["education", "programming"]
        }
    }

    shallow_copy = copy(orignial)

    orignial["author"].append("john")
    orignial["details"]["genre"].append("computer")

    print(orignial)
    print(shallow_copy)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.


def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    book1 = Book("the hobbit", "J.R.R Tolkien", 310)

    print(book1.book_info())
    print(f"book type: {Book.book_type}")

    print("\nTODO: Create and test your child object")


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()