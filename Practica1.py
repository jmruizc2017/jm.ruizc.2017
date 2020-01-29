

#!/usr/bin/python3

file = "/etc/passwd"
file_object = open(file, 'r')
lines = file_object.readlines()
print(lines)
