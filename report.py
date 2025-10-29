
def available_books(library):
   
    print("\n--- AVAILABLE BOOKS ---")
    available = [book for book in library.books.values() if book.available]

    if available:
        for book in available:
            
            print(f"- {book}")
    else:
        print("No books are currently available.")
    print("------------------------")
    pass

def borrowed_books(library):
    

    print("\n--- BORROWED BOOKS ---")
    borrowed = [book for book in library.books.values() if not book.available]
    
    if borrowed:
        for book in borrowed:
            
            print(f"- {book}")
    else:
        print("No books are currently borrowed.")
    print("-----------------------")
    pass

def member_report(member):
   
    print(f"\n--- MEMBER REPORT: {member.name} ---")
    print(f"Member ID: {member.member_id}")
    
    if member.borrowed_books:
        print(f"Borrowed Books ({len(member.borrowed_books)}):")
        for book in member.borrowed_books:
            print(f"  - {book.title} by {book.author}")
    else:
        print(f"{member.name} has no books currently borrowed.")
    print("-----------------------------------")
    pass
