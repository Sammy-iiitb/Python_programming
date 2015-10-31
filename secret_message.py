import os
from os import listdir
from os.path import isfile, join
#mypath = os.path.dirname(os.path.abspath(__file__))
mypath = "/home/samyak/Udacity/python_programming/prank"
def rename_files():
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f))]
	#print onlyfiles
	newfiles = []
	for s in onlyfiles:
		result = ''.join([i for i in s if not i.isdigit()])
		#print result
		newfiles.append(result)
	#print newfiles
	i = 0
	for i in range(0,len(onlyfiles)):
		os.rename(onlyfiles[i], newfiles[i])
rename_files()
