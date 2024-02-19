class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        self.file.seek(0)  

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            book_info = book.split(", ")
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter first release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title}, {author}, {release_year}, {pages}\n"
        self.file.write(book_info)
        self.file.flush()

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        books = [book for book in books if not book.startswith(title_to_remove)]
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            self.file.write(book + "\n")
        self.file.flush()

def main():
    lib = Library()
    while True:
        print("*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
