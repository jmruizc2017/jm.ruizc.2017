

#!/usr/bin/python3

file = "/etc/passwd"
file_object = open(file, 'r')
lines = file_object.readlines()
print(lines)
lines.split(',')

file = "/etc/passwd"
>>> lines = file_object.readlines()
>>> file = "/etc/passwd"
>>> file_object = open(file, 'r')
>>> lines = file_object.read()
>>> print(lines)

