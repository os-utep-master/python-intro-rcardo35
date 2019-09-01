import re, os, sys, collections

# Checks if input file exists and it's not empty
def checkFile(input_file):
    if not os.path.exists(input_file):
        print("Input File doesnot exist!")
        exit()

# Reads file, removes white spaces and punctuation characters
# Creates a list of words
def readFile(input_file):
    input_file = open(input_file, 'r').read().lower()
    input_file = re.sub('[^\w]+', ' ', input_file).split()
    return input_file

# Creates a list of words and the amount of occurrences for each
def createList(wordsFile):
    finalList = {}
    for word in wordsFile:
        if word in finalList:
            finalList[word] +=1
        else:
            finalList[word] = 1
    finalList = collections.OrderedDict(sorted(finalList.items()))
    return finalList
    
# Writes words and count to a file
def createOutputFile(wordList):
    output_file = open(outputFile, 'w')
    for word, count in wordList.items():
        output_file.write("{} {}\n".format(word, count))
    output_file.close()

# Script starts here
# Starts by checking if input arguments format is correct
if len(sys.argv) != 3:
    print("\nCorrect Usage: wordCount.py <input text file> <output text file> \nExample: wordCount.py input.txt output.txt\n")
    exit()
else:
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    checkFile(inputFile)
    wordList = readFile(inputFile)
    wordList = createList(wordList)
    createOutputFile(wordList) 