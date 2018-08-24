#!/usr/local/bin/python

# Describe : IO operator



#use with to read file
#with can close file when throw exception
def Read(fileName):
    with open(fileName, 'r') as fileHandler:
        return fileHandler.read()



#read context line by line
def ReadLine(fileName):
    lineList = []
    with open(fileName, 'r') as fileHandler:
        for line in fileHandler.readlines():
            lineList.append(line)
    return lineList



#use with to write file
def Write(fileName, fileData):
    with open(fileName, 'w') as fileHandler:
        fileHandler.write(fileData)