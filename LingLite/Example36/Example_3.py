#!/usr/local/bin/python

# Describe : Serialization

import pickle



def Dumps(sourceFileName, resultFileName):
    with open(sourceFileName, 'r') as sourceFile:
        fileData = sourceFile.read()
        d = {sourceFileName, fileData}
        pickleString = pickle.dumps(d)
        with open(resultFileName, 'wb') as resultFileName:
            resultFileName.write(pickleString)



def Dump(DumpData, fileName):
    with open(fileName, 'wb') as fileHandler:
        pickle.dump(DumpData, fileHandler)



def Load(fileName):
    with open(fileName, 'rb') as fileHandler:
        return pickle.load(fileHandler)