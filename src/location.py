
__auth__ = ["Bill Eger"]

from account import Account


class Location():
    name = ""
    address1 = ""
    address2 = ""
    address3 = ""
    city = ""
    state = ""
    zipcode = ""
    latitude = ""
    longitude = ""
    account = ""

    def __init__(self, name=None):
        self.name = name
        self.account = []

    def setAccount(self, accountNumber=None, meterNumber=None):
        index = None
        for i, val in enumerate(self.account):
            if val.getAccount() == str(accountNumber):
                index = i
        
        if index == None:
            newAccount = Account(str(accountNumber))
            newAccount.setMeter(meterNumber)
            self.account.append(newAccount)
        else:
            print "Existing Account: ", self.account[index]
            self.account[index].setMeter(meterNumber)

    def printLoc(self):
        print "Name :", self.name
        for i, val in enumerate(self.account):
            val.printAccount()

def main():
    print "Location: main()"

if __name__=="__main__":
    main()
