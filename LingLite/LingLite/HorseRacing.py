#!/usr/local/bin/python

# Copyright (c) 2018
# All rights reserved.
# Describe : horse racing xml
# Author   : Butler
# Date     : 2018-08-17

import os
import sys
import MySQLDB
import MSSQLDB



class HorseRacing(object):
    """Horse racing test"""

    def __init__(self):
        self.mysqlInsertSQL = "INSERT INTO vs_horse_racing_event_cards (event_id, rtp_desc, xml_details) VALUES (%s, '%s', '%s')"
        self.mssqlInsertSQL = "INSERT INTO vs_horse_racing_event_cards (event_id, rtp_desc, xml_details) VALUES (%s, N'%s', N'%s')"

    def GetXMLCommonPath(self):
        XMLCommonPath = sys.path[0]
        XMLCommonPath += '\\DataSource\\'
        return XMLCommonPath

    def GetXMLDirectoryList(self, XMLCommonPath, isPrintDirectoryList = False):
        XMLDirectoryList = [ (XMLCommonPath + SubDir) for SubDir in os.listdir(XMLCommonPath) if os.path.isdir(XMLCommonPath + SubDir)]
        if isPrintDirectoryList:
            for XMLDirectory in XMLDirectoryList:
                print("sub directory = " + XMLDirectory)
            print('\n')
        return XMLDirectoryList

    def ReadXMLData(self, XMLDirectory, XMLFileName, isPrintFilePath = False):
        DotIndex = XMLFileName.find('.')
        EventID = XMLFileName[DotIndex - 4 : DotIndex]
        XMLFilePath = XMLDirectory + "\\" + XMLFileName
        print("file path = " + XMLFilePath + ", eventID = " + EventID)
        FileHandler = open(XMLFilePath, 'rb')
        XMLData = FileHandler.read().decode('utf-16')
        return EventID, XMLData

    def WriteXMLToDB(self):
        mysqldb = MySQLDB.MySQLDB('localhost', 3306, 'root', '******', 'test', 'utf8')
        mssqldb = MSSQLDB.MSSQLDB('192.168.3.19',"sa",'****','test')

        mysqlConnection = mysqldb.GetConnection()
        mssqlConnection = mssqldb.GetConnection()

        mysqldb.Execute('truncate table vs_horse_racing_event_cards')
        mssqldb.Execute('truncate table vs_horse_racing_event_cards')

        XMLDirectoryList = self.GetXMLDirectoryList(self.GetXMLCommonPath(), True)
        for XMLDirectory in XMLDirectoryList:
            XMLList = os.listdir(XMLDirectory)
            RTP = (XMLDirectory.split('\\')[-1]).split(' ')[0]

            for XMLFileName in XMLList:
                EventID, XMLData = self.ReadXMLData(XMLDirectory,XMLFileName)
                SQLValue = (EventID, RTP, XMLData)

                mysqldb.WriteToDB(self.mysqlInsertSQL, SQLValue)
                mssqldb.WriteToDB(self.mssqlInsertSQL, SQLValue)
