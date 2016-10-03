#!/usr/bin/python3

fp = open("A Tale of 2 Cities", "r")
info = open(fp.name + ".info", "r")
print ("Name of file: ", fp.name)
print ("------------------------------")
str = fp.read()
#strTwo = info.read()


lineRead = info.readline() 
if lineRead[0] == "B":
	print ("Bold 1")
	lineRead = lineRead.strip("B ")
	modBold = lineRead
	modBold = lineRead.strip("\n")

	#modBold = "<B>{0}</B>".format(lineRead)
	modBold = "<B>%s</B>" % modBold
	#print (str.find(lineRead))
	#newStr = "<B>{0}</B>".format(lineRead)
	print ("!" + modBold + "!")
	print (str.find(lineRead))

elif lineRead[0] == "U":
	print ("Under 1")
elif lineRead[0] == "I":
	print ("Italic 1")


while lineRead:
	print (lineRead)
	lineRead = info.readline()

	for under in lineRead:
		if under[0] == "U":
			print ("Under in")
			lineRead = lineRead.strip("U ")
			print (str.find(lineRead))

		elif under[0] == "B":
			print ("Bold in")

		elif under[0] == "I":
			print ("Italic in")
			lineRead = lineRead.strip("I ")
			#print (str.find(lineRead))
			modIt = lineRead
			print ("!" + modIt + "!")




info.close()
fp.close()
