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
        self.isbookavailable = True
