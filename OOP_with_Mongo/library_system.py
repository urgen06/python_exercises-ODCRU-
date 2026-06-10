from pymongo import MongoClient

class Library:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["library"]
    books = db["books"] 

    def add_book(self):
        title = input("Enter book title: ").lower()
        author = input("Enter author: ").lower()
        is_available = input("Is Available (True or False)?").lower() == "true"
        
        book = Book(title,author,is_available)
        self.books.insert_one(book.to_dict())
        print(f"{title} added successfully!")

    def search_book(self):
        author = input("Find books of author: ").lower()
        results = list(self.books.find({"author": author}))
        if not results:                        
            print("No books found!")
        else:
            for book in results:
                print(f"Title: {book['title']} | Author: {book['author']} | Available: {book['is_available']}")  

    
    def update_book(self):
        title = input("Enter title to update: ").lower()
        new_title = input("Enter new title: ").lower()
        new_author = input("Enter new author: ").lower()
        new_isavailable = input("Is this book available (True or False)? ").lower() == "true"
        result = self.books.update_one(
            {"title": title},
            {"$set": {"title": new_title, "author": new_author, "is_available": new_isavailable}}
            )
        
        if result.modified_count > 0:
            print(f"{title} updated successfully!")
        else:
            print(f"{title} book not found!")
    
    def delete_book(self):
        title = input("Enter title to delete: ").lower()
        result = self.books.delete_one({"title": title})
        if result.deleted_count > 0:
            print(f"{title} book deleted successfully!")
        else:
            print(f"{title} not found!")




class Book:
    
    def __init__(self,title,author,is_available=True):
        if not title:
            raise ValueError("Title cannot be empty!")
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Available: {self.is_available}"
    
    def to_dict(self):
        return{
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available
        }

library = Library()

while True:
    print("\n-- Library Menu --")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Quit")

    choice = input("Choose operation: ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice!")

    elif choice == "1":
        library.add_book()

    elif choice == "2":
        library.search_book()

    elif choice == "3":
        library.update_book()

    elif choice == "4":
        library.delete_book()

    elif choice == "5":
        print("Goodbye!")
        break