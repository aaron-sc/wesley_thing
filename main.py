import os
# below is if you need to be promted each time
# dest = (input("Destination: ")

# Copy
dest = "/path/to/file/"
command = os.popen('cp /path/to/file/* ' + str(dest))
print(command.read())
print(command.close())

# Delete
command = os.popen('rm -r '+ str(dest))
print(command.read())
print(command.close())

print("Complete!")