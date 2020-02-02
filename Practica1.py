
#!/usr/bin/python3

file = "/etc/passwd"
file_object = open(file, 'r')
lines = file_object.readline()
while len(lines) != 0:
    line = lines.split(':')
    print('Usuario:', line[0], '| Shell:', line[-1])
    lines = file_object.readline()
