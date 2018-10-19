
# jsonToMarkdown
# David Lawrence
# 2018
# requires Python 2.7

import datetime
import collections


jsonDataType = ["string", "number", "object", "array", "true", "false", "null"]

boundaries = ["{", ":", ",", "}", "[", "]", "\"", "t", "e", "f", "n", "l", "0"]




currentDataType = -1
currentValue = -1

# function returns the top item in a stack but does not remove it from the stack
def top(someList):
		if len(someList) > 0:
			return someList[len(someList)-1]
		else:
			return ""

def setUpTable(outputFile):
	outputFile.write("| Field       | Type    | Description  |\n")
	outputFile.write("|-------------|---------|--------------|\n")


# iterate through each character in a JSON file, write results to report file, and append Markdown to another file
def parseJsonFile(jsonFile, outputReportFile, outputMarkdownFile):
	#get a file handle for JSON file
	jsonFile = open(jsonFile, 'r')


	jsonSource = jsonFile.read()

	reportFile = open(outputReportFile, 'w')

	outputMarkdownFile = open(outputMarkdownFile, 'w')

	# print current date and time at top of document
	i = datetime.datetime.now()
	reportFile.write(str(i))
	reportFile.write("\n\n")
	reportFile.write("in parseJsonFile function; preparing to iterate through json\n\n")
	print("preparing to iterate through json")

	## set initial context

	# make a list to hold a stack of objects and arrays
	#  this can be referred to to determine the collection containing the current character
	# using collectionStack[len(collectionStack)-1]
	collectionStack = [] # possible values: "object" or "array"


	positionStack = [1] # create stack list with 1 signifying start of JSON

	currentCollection = 0

	boundaryStack = [] # possible values are anything in 'boundaries' list

	# set up string buffer
	stringBuffer = ''

	# set up variables to describe each response field
	objectValueName = ''
	objectValueType = ''

	objectValueNameTypeStack = []
	objectValueNameContext = ''


	tableRows = []

	setUpTable(outputMarkdownFile)


	for i, c in enumerate(jsonSource):
	
		if c == '{':
			if top(positionStack) == 9:
				if top(objectValueNameTypeStack) != "[#]":
					objectValueNameTypeStack.append("[#]")
			elif top(positionStack) == 5:
				outputMarkdownFile.write("| " + objectValueNameContext + " | Object |   |\n")

			positionStack.append(2)	
			reportFile.write(str(i) + "   " + c + "   " + "object start")
			reportFile.write("\n")					
			print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)


		elif c == '}':
			if top(positionStack) == 2: #if in the object position
				positionStack.pop()     # pop the object position off the stack 
				if len(objectValueNameTypeStack) != 0:
					objectValueNameTypeStack.pop()

			elif top(positionStack) == 5:
				positionStack.pop()    # pop the objectValue position off the stack
				positionStack.pop()    # pop the object position off the stack
				if len(objectValueNameTypeStack) != 0:
					objectValueNameTypeStack.pop()
			elif top(positionStack) == 6 or top(positionStack) == 7 or top(positionStack) == 8 or top(positionStack) == 9:
				positionStack.pop()    # pop the objectValueString, objectValueInteger, objectValueTrueFalseNull or array position off the stack
				positionStack.pop()    # pop the objectValue position off the stack
				positionStack.pop()    # pop the object position off the stack
				if len(objectValueNameTypeStack) != 0:
					objectValueNameTypeStack.pop()
			print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)
			reportFile.write(str(i) + "   " + c + "   " + "object close")
			reportFile.write("\n")	

			print "                " + str(objectValueNameTypeStack)


		elif c == '[':
			if top(positionStack) == 5:
				outputMarkdownFile.write("| " + objectValueNameContext + " | Array |   |\n")
			positionStack.append(9)
			print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)
			reportFile.write(str(i) + "   " + c + "   " + "array start")
			reportFile.write("\n")	

		elif c == ']':
			if len(objectValueNameTypeStack) != 0:
					objectValueNameTypeStack.pop()
			positionStack.pop()
			#print "     at position " + str(i) + " positionStack is now: " + str(positionStack)
			reportFile.write(str(i) + "   " + c + "   " + "array close")
			reportFile.write("\n")	
			print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)
			print "                " + str(objectValueNameTypeStack)

		elif c == '"':
			if top(positionStack) == 4: #if in the object value name string position
				objectValueName = stringBuffer
				objectValueNameTypeStack.append(objectValueName)

				stringBuffer = ''

				objectValueNameContext = ".".join(objectValueNameTypeStack) #build a string from the ancestor value names in reverse order
				objectValueNameContext = objectValueNameContext.replace(".[#]", "[#]")
				

				positionStack.pop()     # pop the string position off the stack

				print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack) + " and object value name is: " + objectValueName
				objectValueName = ''

			elif top(positionStack) == 2: #if in the object position (start)
				positionStack.append(3)
				positionStack.append(4)
				print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)
				
			elif top(positionStack) == 3: #if in the objectValueName position
				positionStack.append(4)   # put the object value name string position on the stack
				print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)
				
			elif top(positionStack) == 5: #if in the objectValue position 
				objectValueNameTypeStack.pop() # remove the last item (the name for this name-value pair) from the ancestor stack
				positionStack.append(6)   # put the object value string position on the stack
				print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)

				outputMarkdownFile.write("| " + objectValueNameContext + " | String |   |\n")
			
			elif top(positionStack) == 6: #if in the objectValueString position 
				positionStack.pop()   # pop the objectValue string position
				print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)


			reportFile.write(str(i) + "   " + c + "   " + "String start or close")
			reportFile.write("\n")

			print "                " + str(objectValueNameTypeStack)
			

			objectValueName = ''

		elif c == ':':
			if top(positionStack) == 3:
				positionStack.pop() # pop the objectName position off the stack
				positionStack.append(5) # put objectValue position on the stack
			reportFile.write(str(i) + "   " + c + "   " + "Object name-value delimiter")
			reportFile.write("\n")
			print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)
			if top(positionStack) == 5:
				stringBuffer = ''

		elif c == ',':
			if top(positionStack) == 5:
				positionStack.pop()    # pop the objectValue position off the stack
				positionStack.append(3) # put objectValueName position on the stack
			elif top(positionStack) == 7 or top(positionStack) == 8:
				positionStack.pop()    # pop the objectValueString, objectValueInteger, or objectValueTrueFalseNull position off the stack
				positionStack.pop()    # pop the objectValue position off the stack
				positionStack.append(3) # put objectValueName position on the stack
			elif top(positionStack) == 8: #if object value is true, false, or null
				positionStack.pop()    # pop the object value true-false-null position off the stack
				positionStack.pop()    # pop the object value position off the stack

			reportFile.write(str(i) + "   " + c + "   " + "Object or array member delimiter")
			reportFile.write("\n")
			#if top(positionStack) == 4:
				#stringBuffer = stringBuffer + c
			print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)

			print "                " + str(objectValueNameTypeStack)

		elif c == '\n':
			reportFile.write(str(i) + "   " + " " + "   " + "newline")
			reportFile.write("\n")

		elif c.isdigit():
			reportFile.write(str(i) + "   " + c + "   " + "number")
			reportFile.write("\n")
			if top(positionStack) == 4:
				stringBuffer = stringBuffer + c
			elif top(positionStack) == 5:
				positionStack.append(7)
				print "   " + c + " at position " + str(i) + " positionStack is now: " + str(positionStack)

				outputMarkdownFile.write("| " + objectValueNameContext + " | Number |   |\n")

				objectValueNameTypeStack.pop() # this is a number value, so name-value pair has no children. Remove it from ancestor stack.
				print "                " + str(objectValueNameTypeStack)

		elif c.isalpha():
			reportFile.write(str(i) + "   " + c + "   " + "letter")
			reportFile.write("\n")
			if top(positionStack) == 4:
				stringBuffer = stringBuffer + c
			elif top(positionStack) == 5:
				positionStack.append(8)
				outputMarkdownFile.write("| " + objectValueNameContext + " | *true*, *false*, *null* |   |\n")
				objectValueNameTypeStack.pop() # this is a true / false / null value, so name-value pair has no children. Remove it from ancestor stack.
		# elif c.isspace():
		# 	pass
		# else:
		# 	reportFile.write(str(i) + "   " + c + "   " + "something else")


		characterCount = i

	return characterCount

def removeDuplicateLines(inputFile, outputFile):
	#from Stack Overflow top-rated answer: 
	#   https://stackoverflow.com/questions/1215208/how-might-i-remove-duplicate-lines-from-a-file
	linesSeen = set() 
	outfile = open(outputFile, "w")
	for line in open(inputFile, "r"):
		if line not in linesSeen: #line is not a duplicate
			outfile.write(line)
			linesSeen.add(line)
	outfile.close()


def removeDuplicateLinesRetainOrder(inputFile, outputFile):
	#from Stack Overflow top-rated answer: 
	#   https://stackoverflow.com/questions/1215208/how-might-i-remove-duplicate-lines-from-a-file

	lines_seen = set() # holds lines already seen
	outfile = open(outputFile, "w")
	previousLine = ""

	with open(inputFile, "r") as inFile:
		inBuffer = inFile.readlines()

	outBuffer = ""

	for line in inBuffer:
	    if line not in lines_seen: # not a duplicate
	    	outBuffer = outBuffer.replace(previousLine, previousLine + line)
	        lines_seen.add(line)
	    previousLine = line
	
	with open(outputFile, "w") as outFile:
		outFile.write(outBuffer)



