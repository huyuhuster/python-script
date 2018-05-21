file = open('abs.txt','r')
 
while 1:
    lines = file.readlines(1)
    if not lines:
        break
    for line in lines:
        print line
