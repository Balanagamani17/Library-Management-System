import sys
from library import Library
from book import Book
from member import Member
from exceptions import BookNotFoundError, BookNotAvailableError, MemberNotFoundError
from utils import generate_id
from report import available_books, borrowed_books, member_report
def _add_book(library):
    
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    
    if not title or not author:
        print("Title and Author cannot be empty. Book creation failed.")
        return
    book_id = generate_id("BOOK")
    
    new_book = Book(book_id, title, author)
    library.add_book(new_book)

def _add_member(library):
   
    name = input("Enter member name: ").strip()
    
    if not name:
        print("Member name cannot be empty. Member creation failed.")
        return
    member_id = generate_id("MEM")
    
    new_member = Member(member_id, name)
    library.add_member(new_member)

def _borrow_book(library):
   
    member_id = input("Enter Member ID: ").strip().upper()
    book_id = input("Enter Book ID to borrow: ").strip().upper()

    try:
        library.borrow_book(member_id, book_id)
    except (MemberNotFoundError, BookNotFoundError, BookNotAvailableError) as e:
        print(f"\nERROR: {e}")

def _return_book(library):
    
    member_id = input("Enter Member ID: ").strip().upper()
    book_id = input("Enter Book ID to return: ").strip().upper()

    try:
        library.return_book(member_id, book_id)
    except (MemberNotFoundError, BookNotFoundError) as e:
        print(f"\nERROR: {e}")

def _view_reports(library):
    
    while True:
        print("\n--- REPORTS ---")
        print("1. Available Books")
        print("2. Borrowed Books")
        print("3. Member Report")
        print("4. Back to Main Menu")
        
        report_choice = input("Enter report choice: ").strip()

        if report_choice == "1":
            available_books(library)
        elif report_choice == "2":
            borrowed_books(library)
        elif report_choice == "3":
            member_id = input("Enter Member ID for report: ").strip().upper()
            if member_id in library.members:
                member_report(library.members[member_id])
            else:
                print(f"Member ID '{member_id}' not found.")
        elif report_choice == "4":
            break
        else:
            print("Invalid report choice.")

def main():
    
    library = Library()
    print("Library Management System Initialized.")
    _load_sample_data(library)
    
    while True:
        print("\n=============== LIBRARY MENU ===============")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Reports")
        print("6. Exit")
        print("============================================")
        
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            _add_book(library)
        elif choice == "2":
            _add_member(library)
        elif choice == "3":
            _borrow_book(library)
        elif choice == "4":
            _return_book(library)
        elif choice == "5":
            _view_reports(library)
        elif choice == "6":
            print("Exiting Library System. Goodbye! 👋")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
def _load_sample_data(library):
    b1 = Book("BOOK-001", "The Martian", "Andy Weir")
    b2 = Book("BOOK-002", "Dune", "Frank Herbert")
    b3 = Book("BOOK-003", "Pride and Prejudice", "Jane Austen")
    
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    
  
    m1 = Member("MEM-101", "Alice")
    m2 = Member("MEM-102", "Bob")
    
    library.add_member(m1)
    library.add_member(m2)

    
    try:
        library.borrow_book("MEM-101", "BOOK-001")
    except Exception as e:
        
        print(f"Error loading sample data: {e}")
    pass

if __name__ == "__main__":
    main()
