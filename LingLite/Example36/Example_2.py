#!/usr/local/bin/python

# Describe : file and directory

import os
import shutil



def TestFileAndDirectory():
    environment = os.getenv('PATH')                                     #��������
    print("Current environment:\n" + environment + "\n")

    print("Current OS:\n" + os.name + "\n");                            #��ǰϵͳ��
    print("Current line sep:\n" + str(os.linesep) + "\n")                #��ǰϵͳ������ֹ��

    currentWorkDirectory = os.getcwd()                                  #����Ŀ¼·��
    print("Current work directory:\n" + currentWorkDirectory + "\n")

    DirectoryAndFileList = os.path.split(currentWorkDirectory)          #����Ŀ¼���ļ���
    print("Split directory and file name:\n" + str(DirectoryAndFileList) + "\n")

    filesList = os.listdir();                                           #Ŀ¼�µ��ļ���Ŀ¼
    print("Directory files list:\n" + str(filesList) + "\n")

    for filepath in filesList:
        if os.path.exists(filepath) == False:                           #У��·���Ƿ���Ĵ���
            continue

        if os.path.isabs(filepath):                                     #�Ƿ��Ǿ���·��
            print("Absolute path:" + filepath + "\n")

        if os.path.isfile(filepath):                                    #�Ƿ����ļ�
            if filepath == "test.txt":
                os.remove(filepath)                                     #ɾ���ļ�

        if os.path.isdir(filepath):                                     #�Ƿ���Ŀ¼
            if filepath == "test":
                os.removedirs(filepath)                                 #ɾ����Ŀ¼

        if filepath == "oldname":
            os.rename(filepath, "newname")                              #������

        print("Directory name: " + os.path.dirname(filepath))            #·����
        print("file name: " + os.path.basename(filepath))                #�ļ���
        print("Split name: " + str(os.path.splitext(filepath)))          #������չ��
        print("file size: " + str(os.path.getsize(filepath)))            #��ȡ�ļ���С
        print("file stat: " + str(os.stat(filepath))  + "\n")            #��ȡ�ļ�����
        #print("file chmod:\n" + str(os.chmod(filepath)) + "\n")         #�޸��ļ�Ȩ����ʱ���

    singledir = r"singledir"
    multiDir = currentWorkDirectory + r"\multidir"
    os.makedirs(multiDir)                                               #�����༶Ŀ¼
    os.mkdir(singledir)                                                 #��������Ŀ¼

    oldDirectory = filesList[-1]
    newDirectory = filesList[-1] + "Temp"
    shutil.copytree(oldDirectory, newDirectory)                         #�����ļ���
    shutil.copy(filesList[0], newDirectory)                             #�����ļ�

    shutil.move(newDirectory, multiDir)                                 #�ƶ��ļ��л��ļ�

    os.rmdir(singledir)                                                 #ֻ��ɾ����Ŀ¼
    shutil.rmtree(multiDir)                                             #ɾ��ȫ��
