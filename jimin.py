class Book:
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = available
    
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        if isinstance(new_isbn, int) and new_isbn > 0:
            self.__isbn = new_isbn 
            print("ISBN updated successfully.")
        else:
            print("Invalid ISBN. Please enter a positive integer.")
        

    def our_books(self):
        print(f"book Title: {self.title}, \n  Author: {self.author}, \n ISBN: {self.__isbn}, \n Available: {self.available}")

book1 = Book("Twisted Love", "Ana Huang", 640, True)
book2 = Book("Twisted game", "Ana Huang", 134, True)
book3 = Book("King of Wrath", "Ana Huang", 365, True)
book4 = Book("Hunting Adeline", "H. D. Carlton", 13, False)

book1.our_books()
book2.our_books()
book3.our_books()
book4.our_books()




class Member:
    def __init__(self, name, member_id, borrowed_books):
        self.name = name
        self.__member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
    
    def member_info(self):
        print(f"Name: {self.name}, \n Member ID: {self.__member_id}, \n Borrowed Books: {self.borrowed_books}")


    def borrow_book(self, book_title):
       if book_title not in self.borrowed_books:
           self.borrowed_books.append(book_title)
           print(f"{self.name} borrowed {book_title}")
       else:
           print(f"{self.name} already borrowed {book_title}")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            print(f"{self.name} returned {book_title}")
        else:
            print(f"{self.name} doesn't have {book_title} borrowed")



member1 = Member("Jimin", 13, ["Twisted Love"])
member2 = Member("Taehyung", 30, ["King of Wrath"])
member3 = Member("Jungkook", 97, ["Hunting Adeline"])
member4 = Member("Seokjin", 92, ["Shatter Me"])


member1.member_info()
member2.member_info()
member3.member_info()
member4.member_info()


class StaffMember(Member):
    def __init__(self, name, member_id, staff_id):
        super().__init__(name, member_id, [])
        self.staff_id = staff_id

    def add_book(self, book):
        print(f"Staff Member {self.name} \n added the book: {book.title}")

staff1 = StaffMember("Namjoon", 201, "S001")
staff2 = StaffMember("Hoseok", 202, "S002")
staff3 = StaffMember("Yoongi", 203, "S003")

staff1.add_book(book4)
staff2.add_book(book2)


book5 = Book("Harry Potter", "J.K. Rowling", 500, True)
staff3.add_book(book5)

