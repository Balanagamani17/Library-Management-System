class Member:
    def __init__(self, member_id, name):
       

        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  

        pass

    def borrow_book(self, book):
       

        self.borrowed_books.append(book)

        pass

    def return_book(self, book_id):
        

        book_to_return = None
        for book in self.borrowed_books:
            if book.book_id == book_id:
                book_to_return = book
                break

        if book_to_return:
            self.borrowed_books.remove(book_to_return)
            return book_to_return
        return None 

    def __str__(self):
       

        return f"Member[{self.member_id}] - {self.name} (Books: {len(self.borrowed_books)})"
    
    def __repr__(self):
        return self.__str__()
