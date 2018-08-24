#!/usr/local/bin/python

# Describe : file and directory

import os
import shutil



def TestFileAndDirectory():
    environment = os.getenv('PATH')                                     #环境变量
    print("Current environment:\n" + environment + "\n")

    print("Current OS:\n" + os.name + "\n");                            #当前系统名
    print("Current line sep:\n" + str(os.linesep) + "\n")                #当前系统的行终止符

    currentWorkDirectory = os.getcwd()                                  #工作目录路径
    print("Current work directory:\n" + currentWorkDirectory + "\n")

    DirectoryAndFileList = os.path.split(currentWorkDirectory)          #分离目录和文件名
    print("Split directory and file name:\n" + str(DirectoryAndFileList) + "\n")

    filesList = os.listdir();                                           #目录下的文件和目录
    print("Directory files list:\n" + str(filesList) + "\n")

    for filepath in filesList:
        if os.path.exists(filepath) == False:                           #校验路径是否真的存在
            continue

        if os.path.isabs(filepath):                                     #是否是绝对路径
            print("Absolute path:" + filepath + "\n")

        if os.path.isfile(filepath):                                    #是否是文件
            if filepath == "test.txt":
                os.remove(filepath)                                     #删除文件

        if os.path.isdir(filepath):                                     #是否是目录
            if filepath == "test":
                os.removedirs(filepath)                                 #删除空目录

        if filepath == "oldname":
            os.rename(filepath, "newname")                              #重命名

        print("Directory name: " + os.path.dirname(filepath))            #路径名
        print("file name: " + os.path.basename(filepath))                #文件名
        print("Split name: " + str(os.path.splitext(filepath)))          #分离扩展名
        print("file size: " + str(os.path.getsize(filepath)))            #获取文件大小
        print("file stat: " + str(os.stat(filepath))  + "\n")            #获取文件属性
        #print("file chmod:\n" + str(os.chmod(filepath)) + "\n")         #修改文件权限与时间戳

    singledir = r"singledir"
    multiDir = currentWorkDirectory + r"\multidir"
    os.makedirs(multiDir)                                               #创建多级目录
    os.mkdir(singledir)                                                 #创建单级目录

    oldDirectory = filesList[-1]
    newDirectory = filesList[-1] + "Temp"
    shutil.copytree(oldDirectory, newDirectory)                         #复制文件夹
    shutil.copy(filesList[0], newDirectory)                             #复制文件

    shutil.move(newDirectory, multiDir)                                 #移动文件夹或文件

    os.rmdir(singledir)                                                 #只能删除空目录
    shutil.rmtree(multiDir)                                             #删除全部
