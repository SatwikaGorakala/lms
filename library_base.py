class Book:
    def __init__(self,book_id:int,book_title:str,book_author:str):
        if not isinstance(book_id, int):
            raise TypeError("book_id must be integer")
        if not isinstance(book_title, str):
            raise TypeError("book_title must be string")
        if not isinstance(book_author, str):
            raise TypeError("book_author must be string")
        self.book_id=book_id
        self.book_title=book_title
        self.book_author=book_author
        #self.isbookavailable = True


class Member:
    def __init__(self,member_id:int,member_name:str):
        if not isinstance(member_id, int):
            raise TypeError("member_id must be integer")
        if not isinstance(member_name, str):
            raise TypeError("member_name must be sting")
        self.member_name=member_name # propery to add member name
        self.member_id=member_id # propery to add member id
        self.borrowed_books_bymember=[] # propery to map memberid  to bookids borrowed
        self.maxlimit=0


class Library:
    def __init__(self):
        self.librarybooks={}#dictionary -key , value 
        self.librarymembers={}

    def add_books(self,book_id:int,book_title:str,book_author:str):
        if not isinstance(book_id, int):
            raise TypeError("book_id must be integer")
        if not isinstance(book_title, str):
            raise TypeError("book_title must be string")
        if not isinstance(book_author, str):
            raise TypeError("book_author must be string")
        #below line creates a book class object with  details like id, title, author
        b1 = Book(book_id,book_title,book_author)
        #below line add book object to the dictionary librarybooks and store book object against key bookid
        if book_id not in self.librarybooks: # check of key (book_id) is present in librarybooks dictionary
            self.librarybooks[book_id]= b1
            print(self.librarybooks[book_id].book_author)
            print(self.librarybooks[book_id].book_title)
        else:
            print("book already exists")

    def add_members(self,member_id: int,member_name: str):
        if not isinstance(member_id, int):
            raise TypeError("member_id must be integer")
        if not isinstance(member_name, str):
            raise TypeError("member_name must be sting")
        m1 = Member(member_name,member_id)
        if member_id not in self.librarymembers:
            self.librarymembers[member_id] = m1  #how you are adding items to dictionary
            output = self.librarymembers[member_id]
            print(self.librarymembers[member_id].member_id)
            print(self.librarymembers[member_id].member_name)
            print(type(self.librarymembers[member_id]))
        else:
            print("member already exist")

    def borrow_books(self,member_id:int,book_id:int):
        if not isinstance(member_id, int):
            raise TypeError("member_id must be integer")
        if not isinstance(book_id, int):
            raise TypeError("book_id must be integer")
        #below line by giving key (memberid) I'm getting member details as object
        if not isinstance(member_id, int):
            raise TypeError("member_id must be integer")
        if not isinstance(book_id, int):
            raise TypeError("book_id must be integer")
        member = self.librarymembers[member_id]
        print(member.maxlimit)
        if book_id in member.borrowed_books_bymember:
            print("book is already given,you are not allowed take multiple books")
        else:
            if(member.maxlimit <3):
                #adds  bookid  to list borrowed_books_bymember 
                member.borrowed_books_bymember.append(book_id) # see how list items are added
                # access maxlimit from member obj and increament counter
                member.maxlimit = member.maxlimit+1
            else:
                print("exceeeded limit to borrow books")
    def return_books(self,member_id:int,book_id:int):
        if not isinstance(member_id, int):
            raise TypeError("member_id must be integer")
        if not isinstance(book_id, int):
            raise TypeError("book_id must be integer")
        member=self.librarymembers[member_id]
        member.borrowed_books_bymember.remove(book_id)
        member.maxlimit = member.maxlimit-1
        print(member.maxlimit)

l1 = Library()

l1.add_books("123","detox","suresh")
l1.add_books(345,"dopamine","kumar")
l1.add_books(123,"detox","suresh")
l1.add_books(678,"shiva","kumar")
l1.add_books(987,"gita","kumar")
l1.add_books(123,"detox","suresh")

l1.add_members(40,"satwika")
l1.add_members('40',"satwika")


l1.borrow_books(40,345) #memberid, bookid
l1.borrow_books(40,123) #memberid, bookid
l1.borrow_books(40,345) #memberid, bookid




l1.borrow_books(40,675) #memberid, bookid
l1.borrow_books(40,987) #memberid, bookid

l1.return_books(40,123)    
                  