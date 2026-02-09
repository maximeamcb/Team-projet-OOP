class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class Librarian(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)

    def add_book(self, library, book):
        library.add_book(book)
        print(f"{self.name} added {book.title} to the library.")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"{self.name} removed {book.title} from the library.")

    def issue_book(self,member, book):
        if book.is_available:
            book.is_available = False
            member.borrowed_books.append(book)
            print (f"Librarian {self.name} issued {book.title} to {member.name}.")
        else:
            print(f"Book is unavailable. Adding {member.name} to the reservation queue.")
            book.reservation_queue.append(member) 

    def notify_member(self, member, message):
        if book.reservation_queue:
            next_member = book.reservation_queue.pop(0)
            print(f"Notification to {next_member.name}: {book.title} is now available!") 

class Administrator(User):
    def approve_membership(self, member, new_id):
        print(f"Administrator {self.name} is creating a new account for {member.name}.") 
        return LibraryMember(member.name, new_id)                 

class LibraryMember(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrowed_books = []
        self.fines = 0

    def search_book(self, title):
        print(f"{self.name} is searching for {title}...")
    
    def request_book(self, book):
        print(f"{self.name} has requested {book.title}.")
        return book 
        
    def reserve_book(self, book):
        if book.is_available:
            print(f"{self.name} has reserved {book.title}.")
            book.is_available = False
            self.borrowed_books.append(book)
        else:
            print(f"{book.title} is currently not available. Adding {self.name} to the reservation queue.")
            book.reservation_queue.append(self)

class Book:
    def __init__(self, isbn, author, title):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.is_available = True
        self.reservation_queue = []

    def __str__(self):
        status = "Available" if self.is_available else "Reserved/Loaned"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"   

if __name__ == "__main__":
    print("--- WELCOME TO THE BIZOU LIBRARY ---")

    my_book = Book("1840227966", "Jane Austen", "Emma")

    admin = Administrator("Temperance", "ADM-01")
    librarian = Librarian("Miss Watson", "LIB-01")
    member_Julia = LibraryMember("Julia", "MEM-01")

    print("\n--- STEP 1: Search and Request ---")
    member_Julia.search_book("Emma")
    requested_book = member_Julia.request_book(my_book)

    print("\n--- STEP 2: Borrowing ---")
    librarian.issue_book(member_Julia, my_book)

    print("\n--- STEP 3: Trying to borrow the same book ---")
    member_clement = LibraryMember("Patrick", "MEM-02")
    librarian.issue_book(member_clement, my_book)

    print("\n--- FINAL STATUS ---")
    print(my_book) 
    print(f"{member_Julia.name} has {len(member_Julia.borrowed_books)} book(s).")