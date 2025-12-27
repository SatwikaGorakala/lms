
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