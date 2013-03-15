__author__ = ["Bill Eger"]

from meter import Meter

class Account():
    accountNumber = ""
    data = []
    meter = ""
    
    def __init__(self, accountNumber=None):
        self.accountNumber = accountNumber
        self.meter = []

    def setMeter(self, meterNumber=None):
        index = None
        
        for i, val in enumerate(self.meter):
            if val.getMeter() == str(meterNumber):
                index = i
            
        if index == None:
            newMeter = Meter(str(meterNumber))
            self.meter.append(newMeter)
        else:
            print "Meter Already Exists"

    def getAccount(self):
        return self.accountNumber
    
    def findMeter(self, meterNumber=None):
        found = None
        if meterNumber == None:
            print "No account number to search."
        else:
            for i, val in enumerate(self.meter):
                if val.getMeter() == str(meterNumber):
                    found = i
        
        return found

    def printAccount(self):
        print "Account: ", self.accountNumber
        for i, val in enumerate(self.meter):
            val.printMeter()

def main():
    print "Account: main()"

if __name__ == "__main__":
    main()
