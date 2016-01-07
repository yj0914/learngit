from sys import argv
script, filename = argv
print "we are goning to erase %r ." % filename
print "if you don't want that , hit CTRL_c"
raw_input(">")
print " opening file"
target = open(filename, 'w+')
target.truncate()
line1 = raw_input("line1")
line2 = raw_input("line2")
target.write(line1)
target.write(line2)
target.close()