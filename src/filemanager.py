import csv
import json
import datetime as dt
from meter import Meter

class switch(object):
	value = None
	def __new__(class_, value):
		class_.value = value
		return True

def case(*args):
	return any((arg == switch.value for arg in args))


class FileManager():

	__type__ = "FileManager"

	def __init__(self):
		self.__type__ = "FileManager"

	def read_CSV(self, _object=None):
		
		print _object

		# Select which type of object is requesting data

		_type = _object.__type__
		print _type

		while switch(_type):
			if case('Meter'):
				print "Meter Type"
				break;
			if case('Account'):
				print 'Account Type'
				break;
			if case('EnergyData'):
				print 'EnergyData Type'
				break;
			if case(None):
				print 'No type specified'
				break;
			print "Specified type does not exist"
			break;
		
	def read_JSON(self):
		print "TODO: read_JSON()"

	def write_CSV(self):
		print "TODO: write_CSV()"

	def write_JSON(self):
		print "TODO: write_JSON()"







def main():
	print "FileManager"

	f = FileManager()
	f.read_CSV('Interval')

	m = Meter()
	f.read_CSV(m)


if __name__ == "__main__":
	main()



