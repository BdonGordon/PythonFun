#!/usr/bin/python3

#mainStr is from the actual file. infoStr is from .info 
def fileEditor( mainStr, infoStr ):
	#str = "A very random mainFp"
	#newData = mainFp.replace("A Tale of 2 Cities", "<B>A Tale of 2 Cities</B>")

	for infoLine in infoStr.split("\n"):
		#newData = infoStr.splitlines()[0]
		if infoLine[0] == "B":
			#strip the Bold tag 
			eraseB = infoLine.strip("B ")
			mainTemp = eraseB
			eraseB = "<B>%s</B>" % eraseB
			#print (mainTemp)
			mainStr = mainStr.replace(mainTemp, eraseB)

		elif infoLine[0] == "U":
			#strip the Bold tag 
			eraseB = infoLine.strip("U ")
			mainTemp = eraseB
			eraseB = "<U>%s</U>" % eraseB
			#print (mainTemp)
			mainStr = mainStr.replace(mainTemp, eraseB)

	return mainStr

if __name__ == "__main__":
	#fp name comes from the C program in the future
	fp = open("A Tale of 2 Cities", "r")
	info = open(fp.name + ".info", "r")
	#print ("Name of file: ", fp.name)
	#print ("------------------------------")
	infoLine = info.read()
	htmlLine = fp.read()

	edittedStr = fileEditor(htmlLine, infoLine)

	info.close()
	fp.close()
	#fileEditor(mainFp, edit)


	fp = open("A Tale of 2 Cities", "w")
	fp.write(edittedStr)
	fp.close