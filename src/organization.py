__auth__ = ["Bill Eger"]


from location import Location

class Organization():

    locations = []

    def __init__(self, orgName=None):
        self.orgName = orgName
        self.locations = []

    def getOrganization(self):
    	print self.orgName

def main():
    print "Location: main()"

    o = Organization("General Services")
    o.getOrganization()


if __name__ == "__main__":
    main()
