from sys import argv

scritp, filename = argv

file = open(filename)
print file.read()