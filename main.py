import os
# below is if you need to be promted each time
# dest = (input("Destination: ")
def copy(starting_dest, ending_dest):
	# Copy
	command = os.popen('cp ' + starting_dest + '*' + ending_dest)
	print(command.read())
	print(command.close())

	# Delete
	command = os.popen('rm -r ' + ending_dest + '*')
	print(command.read())
	print(command.close())
	print("Complete!")