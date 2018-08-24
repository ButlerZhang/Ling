#!/usr/local/bin/python

# Describe : file and directory

import os
import shutil



def TestFileAndDirectory():
    environment = os.getenv('PATH')
    print("Current environment:\n" + environment + "\n")

    print("Current OS:\n" + os.name + "\n");
    print("Current line sep:\n" + str(os.linesep) + "\n")

    currentWorkDirectory = os.getcwd()
    print("Current work directory:\n" + currentWorkDirectory + "\n")

    DirectoryAndFileList = os.path.split(currentWorkDirectory)
    print("Split directory and file name:\n" + str(DirectoryAndFileList) + "\n")

    filesList = os.listdir();
    print("Directory files list:\n" + str(filesList) + "\n")

    for filepath in filesList:
        if os.path.exists(filepath) == False:
            continue

        if os.path.isabs(filepath): 
            print("Absolute path:" + filepath + "\n")

        if os.path.isfile(filepath):
            if filepath == "test.txt":
                os.remove(filepath)

        if os.path.isdir(filepath):
            if filepath == "test":
                os.removedirs(filepath)

        if filepath == "oldname":
            os.rename(filepath, "newname")

        print("Directory name: " + os.path.dirname(filepath))
        print("file name: " + os.path.basename(filepath))
        print("Split name: " + str(os.path.splitext(filepath)))
        print("file size: " + str(os.path.getsize(filepath)))
        print("file stat: " + str(os.stat(filepath))  + "\n")
        #print("file chmod:\n" + str(os.chmod(filepath)) + "\n")

    singledir = r"singledir"
    multiDir = currentWorkDirectory + r"\multidir"
    os.makedirs(multiDir)
    os.mkdir(singledir)

    oldDirectory = filesList[-1]
    newDirectory = filesList[-1] + "Temp"
    shutil.copytree(oldDirectory, newDirectory)
    shutil.copy(filesList[0], newDirectory)

    shutil.move(newDirectory, multiDir)

    os.rmdir(singledir)
    shutil.rmtree(multiDir)
