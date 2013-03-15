from datetime import datetime as dt
import numpy as np

__auth__ = ["Bill Eger"]

## TODO:  Need to add comments and doc language

class UtilityData():
    
    # Attributes
    name = ""
    
    startmo = ""
    startdy = ""
    startyr = ""

    endmo = ""
    enddy = ""
    endyr = ""
    
    periodyr = ""
    periodmo = ""

    startdate = ""
    enddate = ""
    days = ""
    resource = ""
    
    fisyr = ""
    calyr = ""
    
    use = ""
    demand = ""

    totcost = ""

    # Methods

    def __init__(self):
        self.startdate = ""
        self.enddate = ""
        self.use = np.NaN
        self.demand = np.NaN
        self.totcost = np.NaN
        self.len = 5


        print "UtilityData object created."
    
    def __getitem__(self, key):

        # From: http://stackoverflow.com/questions/2936863/python-implementing-slicing-in-getitem
        if isinstance(key, slice):
            return [self[ii] for ii in xrange(*key.indices(len(self)))]
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key >= len(self):
                raise IndexError, "The index (%d) is out of range." %key
            
            # Need to handle what is returned. 
            return key
        else:
            raise TypeError, "Invalid argument type."

    def __len__(self):
        return self.len



    def setStartDate(self, date=None):
        if date != None:
            self.startdate = dt.strptime(date, '%m/%d/%Y')

            self.startmo = self.startdate.month
            self.startdy = self.startdate.day
            self.startyr = self.startdate.year

            if self.startdate.month < 7:
                self.ficyr = self.startyr
            else:
                self.ficyr = int(self.startyr) + 1

            self.calyr = self.startdate.year
        else:
            self.startdate = ""
            self.startmo = ""
            self.startdy = ""
            self.startyr = ""
            self.ficyr = ""

    def getStartDate(self):
        return self.startdate

    def setEndDate(self, date=None):
        if date != None:
            self.enddate = dt.strptime(date, '%m/%d/%Y')

            self.endmo = self.enddate.month
            self.enddy = self.enddate.day
            self.endyr = self.enddate.year
            
        else:
            self.enddate = ""
            self.endmo = ""
            self.enddy = ""
            self.endyr = ""

    def getEndDate(self):
        return self.enddate

    def getFisYear(self):
        return self.fisyr

    def getCalYear(self):
        return self.calyr

    def setUse(self, use=None):
        if use != None:
            self.use = use
        else:
            self.use = np.NaN    

        return self.use

    def getUse(self):
        return self.use

    def setDemand(self, demand=None):
        if demand != None:
            self.demand = demand
        else:
            self.demand = np.NaN

        return self.demand

    def getDemand(self):
        return self.demand

    def setTotCost(self, totcost=None):
        if totcost != None:
            self.totcost = totcost
        else:
            self.totcost = np.NaN
        return self.totcost

    def setUtilityData(self, data = None):
        if (data != None) and (type(data).__name__=='list'):
            self.setStartDate(data[0])
            self.setEndDate(data[1])

            if self.getStartDate() > self.getEndDate():
                self.setStartDate(None)
                self.setEndDate(None)
                status = False
                msg = "End Date cannot be less than Start Date"

            else:
                status = True
                msg = "Success"


            self.setUse(data[2])
            self.setDemand(data[3])
            self.setTotCost(data[4])

        return status, msg

    def getUtilityData(self):
        return self.startdate, self.enddate, self.use, self.demand, self.totcost


def main():

    # Testing.  Need to implement unittests

    ud = UtilityData()
    ud.setStartDate("6/15/2013")
    ud.setEndDate("7/12/2013")
    print ud.getStartDate()
    print ud.getEndDate()
    print ud.setUse(2000)
    print ud.getUse()
    print ud.getUtilityData()
    ux = UtilityData()
    print ux.getUtilityData()
    ux.setTotCost(1000)
    ux.setStartDate("3/12/2012")
    print ux.getUtilityData()

    test = ["3/20/2013", "4/20/2013", "1000", "10", "20000"]

    if ux.setUtilityData(test)[0] == True:
        print ux.setUtilityData(test)[1]
    else:
        print ux.setUtilityData(test)[1]
    print ux.getUtilityData()


if __name__ == "__main__":
    main()
