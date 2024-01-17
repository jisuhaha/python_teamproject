class XMember:
    oid=None
    memberid=None
    pssword=None
    telphone=None
    name=None
    grade=None
    info=None
    carinfo=None    
    def __init__(self, memberid, password, telphone, name, grade, info, carinfo):
        self.memberid=memberid
        self.password=password
        self.telphone=telphone
        self.name=name
        self.grade=grade
        self.info=info
        self.carinfo=carinfo