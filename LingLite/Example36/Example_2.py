#!/usr/local/bin/python

# Describe : file and directory

import os
import shutil



def TestFileAndDirectory():
    print("Current work directory : " + os.getcwd() + "\n")
    print("Current directory list : " + os.listdir() + "\n")

