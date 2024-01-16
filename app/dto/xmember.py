class XMember:
    oid=None
    memberid=None
    password=None
    groupName=None
    groupid=None
    telphone=None
    name=None
    status=None
    carnum=None
    carinfo=None
    createdate=None
    def __init__(self, memberid, password, groupName, groupid, telphone, name, status, carnum, carinfo):
        self.memberid=memberid
        self.password=password
        self.groupName=groupName
        self.groupid=groupid
        self.telphone=telphone
        self.name=name
        self.status=status
        self.carnum=carnum
        self.carinfo=carinfo