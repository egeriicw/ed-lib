from organization import Organization

class Portfolio():

    organizations = []
    
    def __init__(self):
        self.organizations = []

    def addToPortfolio(self, organization=None):
        
    	o = Organization(str(organization))
        self.organizations.append(o)

    def getFromPortfolio(self):
    	return list(org for num, org in enumerate(self.organizations))
    		
def main():
    print "Organization: main()"

    p = Portfolio()

    p.addToPortfolio("General Services")
    print p.getFromPortfolio()

    p.addToPortfolio("RPCA")
    test = p.getFromPortfolio()

if __name__ == "__main__":
    main()
