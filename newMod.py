#!/usr/bin/python3

#mainStr is from the actual file. infoStr is from .info 
def fileEditor( mainStr, infoStr ):

	for infoLine in infoStr.split("\n"):
		if infoLine[0] == "B":
			#strip the Bold tag from .info
			eraseB = infoLine.strip("B ")
			#mainTemp holds the variable to be used in the last step
			mainTemp = eraseB
			#format the string with the tags
			eraseB = "<B>%s</B>" % eraseB
			#manipulate and then return the string from main file
			mainStr = mainStr.replace(mainTemp, eraseB)

		elif infoLine[0] == "U":
			eraseB = infoLine.strip("U ")
			mainTemp = eraseB
			eraseB = "<U>%s</U>" % eraseB
			#print (mainTemp)
			mainStr = mainStr.replace(mainTemp, eraseB)

		elif infoLine[0] == "I":
			eraseB = infoLine.strip("I ")
			mainTemp = eraseB
			eraseB = "<I>%s</I>" % eraseB
			#print (mainTemp)
			mainStr = mainStr.replace(mainTemp, eraseB)

		else:
			continue

	return mainStr

def titleEditor():
	

if __name__ == "__main__":
	#fp name comes from the C program in the future
	#fp = open(C_File_Name_Blah, "r")
	fp = open("A Tale of 2 Cities", "r")
	info = open(fp.name + ".info", "r")
	#print ("Name of file: ", fp.name)
	#print ("------------------------------")
	infoLine = info.read()
	htmlLine = fp.read()

	edittedStr = fileEditor(htmlLine, infoLine)

	info.close()
	fp.close()
	#fp = open(C_File_Name_Blah, "r")
	fp = open("A Tale of 2 Cities", "w")
	fp.seek(0)
	fp.write("<HTML>")
	fp.write("\n\n")
	fp.write("<HEAD>")
	fp.write("\n")
	#fp.write("<TITLE>")
	

	

	#fp.write("</TITLE>")
	fp.write("\n")
	fp.write("</HEAD>")
	fp.write("\n\n")	

	fp.write(edittedStr)
	

	fp.write("\n\n")
	fp.write("</HTML>")

	#print (edittedStr)

	fp.close