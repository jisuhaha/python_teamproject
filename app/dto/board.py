class Board:
    oid=None
    groupOID=None
    groupname=None
    loadingtime=None
    unloadingtime=None
    loadingoid=None
    unloadingoid=None
    weigth_t=None
    cost=None
    driverid=None

    def __init__(self, oid, groupOID, groupname, loadingtime, unloadingtime, loadingoid, unloadingoid, weight_t, dirverid, cost):
        self.oid=oid
        self.groupOID = groupOID
        self.groupname = groupname
        self.loadingtime = loadingtime
        self.unloadingtime = unloadingtime
        self.loadingoid = loadingoid
        self.unloadingoid = unloadingoid
        self.weigth_t = weight_t
        self.cost=cost
        self.driverid=dirverid

