__author__ = ["Bill Eger"]

"""
    Example method description
    
    def diff_rot(ddays,latitude,rot_type=None):

    This function computes the change in longitude over days in degrees.

    Parameters
    -----------
    ddays: float
        Number of days that I want to rotate.
        
    latitude: float or array-like
        heliographic coordinate latitude in Degrees.
        
    rot_type: {None | 'howard' | 'synodic' | 'sidereal' | 'allen'}
        howard: Use values for small magnetic features from Howard et al.
        synodic: Use synodic rotation rate.
        sidereal: Use sidereal rotation rate.
        allen: Use values from Allen, Astrophysical Quantities

    Returns:
    -------
    longditude_delta: ndarray            
        The change in longitude over days (units=degrees)
    
    See Also
    --------
    IDL code equavalent:
        http://hesperia.gsfc.nasa.gov/ssw/gen/idl/solar/diff_rot.pro
    
    Examples
    --------
    Default rotation calculation over two days at 30 degrees latitude:
        rotation = diff_rot(2, 30)
    Defult rotation over two days for a number of latitudes:
        rotation = diff_rot(2, np.linspace(-70, 70, 20))
    With rotation type 'allen':
        rotation = diff_rot(2, np.linspace(-70, 70, 20), 'allen')
"""


import csv
import json
import numpy as np
import pandas as pd
import datetime as dt

class EnergyDataFile():
    # Attributes
    filename = ""
    headerrow = []
    headerset = False
    datalines = []
    numDatalines = ""
    filetype = ""
    
    def __init__(self, filename=None, filetype=None):
        self.filename = filename
        self.headerset = False
        self.filetype = filetype

    def read_GreenButton(self, header=None):
        print "Read GreenButton Data"
        return 0

    def print_File(self):
        print self.headerrow
        print self.datalines

    def read_JSON(self, header=None):
        print "Read JSON"
        return 0

    def read_CSV(self, header=None):
        # Determine what type of input file to import.
        # Ultimately, this should be refactored in to multiple
        # methods with a main controller within this method.

        if self.filetype == "ec":
            print "EnergyCAP file"
        elif self.filetype == "gb":
            print "Green Button file"
        else:
            print "No filetype specified, assume EnergyCAP"
        
        if self.filename != None:
            try:
                with open('../data/input/' + self.filename, 'rb') as infile:
                    print "File: ", self.filename, " Open."
                    if header == None:
                        for line in infile: 
                            self.datalines.append(line.strip('\r\n'))
                    else:
                        for line in infile:
                            # Will need to change the headerset variable
                            # so that users can modify headernames 
                            if self.headerset == False:
                                self.headerrow = line.strip('\r\n').split(',')
                                self.headerset = True
                            else:
                                self.datalines.append(line.strip('\r\n').split(','))

            except IOError as e:
                print "IOException:", e
            finally:
                self.numberDatalines = len(self.datalines) 
                infile.close()
        else:
            print "Must provide filename"


class EnergyData():
    
    # Attributes
    name = ""
    mo = ""
    dy = ""
    yr = ""
    date = ""
    
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

    rate = ""

    # Methods

    def __init__(self):
        print "EnergyData object created."
            
    def setDate(self, mo, dy, yr):
        self.mo = mo
        self.dy = dy
        self.yr = yr
        self.date = dt.datetime(yr, mo, dy)

        if mo < 7:
            self.ficyr = yr
        else:
            self.ficyr = int(yr) + 1

class AuditManager(): 
    print "Audit Manager"

class RateManager():
    print "Rate Manager"

class Energy():
    # Attributes

    ID = ""
    account = ""
    meter = ""
    
    # Methods
    def __init__(self):
        self.account = ""
        self.meter = ""
        self.ID = ""

class Meter():
    meterNumber = ""
    resource = ""
    energy = []

    def __init__(self, meterNumber=None):
        self.meterNumber = meterNumber
        self.resource = ""
        self.energy = []

    def getMeter(self):
        return self.meterNumber

    def printMeter(self):
        print "--Meter: ", self.meterNumber
        print "-------: ", self.resource
        print "-------: ", self.energy

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

class Organization():

    locations = []

    def __init__(self, orgName=None):
        self.orgName = orgName
        self.locations = []

class Portfolio():

    organizations = []
    
    def __init__(self):
        self.organizations = []

    def addOrganization(self, organization=None):
        self.organization.append(Organization())

def main():
    
    edf = EnergyDataFile('EnergyReportingWorkingBook.csv')
    edf.read_CSV(header=True)
    loc = Location("City Hall")
    loc.setAccount("123456789", "11111")
    loc.setAccount("555555555", "55555")
    loc.setAccount("123456789", "22222")
    loc.setAccount("987654321", "33333")
    loc.setAccount("987654321", "33333")
    loc.printLoc()

if __name__ == "__main__":
    main()
