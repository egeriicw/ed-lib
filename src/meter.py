from utilitydata import UtilityData
import numpy as np


__author__ = ["Bill Eger"]

class Meter():
    meterNumber = ""
    resource = ""
    data = []

    __type__ = "Meter"

    def __init__(self, meterNumber=None):
        self.meterNumber = meterNumber
        self.resource = ""
        self.data = []
        self.__type__ = "Meter"

    def __type__(self):
        return self.__type__

    def getMeterNumber(self):
        return self.meterNumber

    def setMeterNumber(self, meterNumber=None):
        self.meterNumber = meterNumber

    def setUtilityData(self, data=None):

        ud = UtilityData()
        ud.setUtilityData(data)

        self.data.append(ud)

        # Need to do some date checking

    def printMeter(self):
        print "--Meter: ", self.meterNumber
        print "-------: ", self.resource
        # Need to figure out how to get only date and value for numpy array
        print "-------: ", [data[1:2] for data in self.data]
        print np.array(self.data)
    


def main():
    m = Meter()

    print m.__type__
    print __file__

    testData = ["3/12/2013", "4/13/2013", "100", "10", "1000"]
    m.setUtilityData(["3/12/2013", "4/13/2013", "100", "10", "1000"])
    m.setUtilityData(["4/13/2013", "5/13/2013", "200", "20", "2000"])
    m.setUtilityData(["6/13/2013", "7/13/2013", "300", "30", "3000"])
    m.printMeter()

if __name__ == "__main__":
    main()
