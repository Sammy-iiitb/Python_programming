import os
def rename_files():
	file_list = os.listdir(r"/home/samyak/Udacity/python_programming/prank")
	#print(file_list)
	saved_path = os.getcwd()
	os.chdir(r"/home/samyak/Udacity/python_programming/prank")
	for filename in file_list:
		os.rename(filename, filename.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()
