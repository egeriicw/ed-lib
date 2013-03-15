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
import re
import unittest

import getpass


##########################
# User-defined libraries #
##########################

from location import Location

class EnergyDataFile():
    # Attributes
    filename = ""
    headerrow = []
    headerset = False
    datalines = []
    numDatalines = ""
    filetype = ""
    oDataDict = dict()
    dicttest = dict()
    __type__ = "EnergyDataFile"


    
    def __init__(self, filename=None, filetype=None):
        self.filename = filename
        self.headerset = False
        self.filetype = filetype
        self.oDataDict = {}
        self.dicttest = {}
        self.__type__ = "EnergyDataFile"

    def __type__(self):
        return self.__type__
        

    def read_GreenButton(self, header=None):
        print "Read GreenButton Data"
        return 0

    def print_Header(self):
        print self.headerrow
    
    def print_Data(self):
        print self.datalines

    def read_JSON(self, header=None):
        print "Read JSON"
        return 0

    def getDict(self):
        from operator import itemgetter
        self.oDataDict.setdefault("Location", {})
        
        labels = []
        account = {}

        for i in range(0, len(self.headerrow)):
            labels.append(self.headerrow[i].replace('(', '').replace(')','').replace(" ", ''))
            
        print labels[4]

        for i, val in enumerate(self.datalines):
            
            account.setdefault("Account", {})
            account["Account"]= {}
            
            #print i
            data = dict(zip(itemgetter(5, 6, 7, 8, 9, 10, 11, 12)(labels), itemgetter(5,6,7,8,9,10,11,12)(val)))
            accountdata = dict(zip(itemgetter(4, 1, 18)(labels), itemgetter(4,1,18)(val)))     
            
            #account["Account"][val[4]] = {}
            if account["Account"].has_key(val[4]):
                account["Account"][val[4]]["data"] = data

            else:
                account["Account"] = accountdata
                account["Account"][val[4]] = {}
                account["Account"][val[4]]["data"] = data
            
                

            print account
            
            #self.oDataDict["Location"][i] = {}
            #self.oDataDict["Location"][i]["data"] = data

        
        #print self.oDataDict
                


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

    def read_CSVDictTest(self, filename=None):
       
        print 'read csv dict test'
        sourcefile = open('../data/input/' + self.filename)

        reader = csv.DictReader(sourcefile)
        reader.next()

        out = json.dumps([row for row in reader])

        jsonFile = open('../data/output/jsontest.json', 'wb')
        jsonFile.write(out)

    def write_JSON(self):
        return 0


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

def main():
    edf = EnergyDataFile('EnergyReportingtest.csv')
    #edf.read_CSV(header=True)
    edf.read_CSVDictTest()
    edf.print_Header()
    #edf.getDict()
    loc = Location("City Hall")
    loc.setAccount("123456789", "11111")
    #loc.setAccount("555555555", "55555")
    #loc.setAccount("123456789", "22222")
    #loc.setAccount("987654321", "33333")
    #loc.setAccount("987654321", "33333")
    loc.printLoc()

    print edf.__type__

if __name__ == "__main__":
    main()

