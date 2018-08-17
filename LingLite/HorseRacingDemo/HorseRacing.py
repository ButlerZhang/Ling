#!/usr/local/bin/python

# Copyright (c) 2018
# All rights reserved.
# Describe : horse racing xml
# Author   : Butler
# Date     : 2018-08-17

import os
import sys
import itertools
import MySQLDB
import MSSQLDB
import HorseRacingExcel
import xml.dom.minidom as xmldom
from enum import Enum



CombinationType = Enum('CombinationType', ('Win', 'Place', 'Exacta', 'Quinella', 'Tierce', 'Trio'))



class HorseRacing(object):
    """Horse racing test"""

    def __init__(self):
        self.__hrExcel = HorseRacingExcel.HorseRacingExcel()
        self.__mysqlInsertSQL = "INSERT INTO vs_horse_racing_event_cards (event_id, rtp_desc, xml_details) VALUES (%s, '%s', '%s')"
        self.__mssqlInsertSQL = "INSERT INTO vs_horse_racing_event_cards (event_id, rtp_desc, xml_details) VALUES (%s, N'%s', N'%s')"

    def GetXMLCommonPath(self):
        XMLCommonPath = sys.path[0]
        XMLCommonPath += "\\DataSource\\"
        return XMLCommonPath

    def GetXMLDirectoryList(self, XMLCommonPath, isPrintDirectoryList=False):
        XMLDirectoryList = [ (XMLCommonPath + SubDir) for SubDir in os.listdir(XMLCommonPath) if os.path.isdir(XMLCommonPath + SubDir)]
        if isPrintDirectoryList:
            for XMLDirectory in XMLDirectoryList:
                print("sub directory = " + XMLDirectory)
            print('\n')
        return XMLDirectoryList

    def ReadXMLData(self, XMLDirectory, XMLFileName, isPrintFilePath=False):
        DotIndex = XMLFileName.find('.')
        EventID = XMLFileName[DotIndex - 4 : DotIndex]
        XMLFilePath = XMLDirectory + "\\" + XMLFileName
        print("file path = " + XMLFilePath + ", eventID = " + EventID)
        FileHandler = open(XMLFilePath, 'rb')
        XMLData = FileHandler.read().decode('utf-16')
        return EventID, XMLData

    def WriteXMLToDB(self):
        mysqldb = MySQLDB.MySQLDB('localhost', 3306, 'root', '*****', 'test', 'utf8')
        mssqldb = MSSQLDB.MSSQLDB('192.168.3.19',"sa",'*****','test')

        mysqlConnection = mysqldb.GetConnection()
        mssqlConnection = mssqldb.GetConnection()

        mysqldb.Execute("truncate table vs_horse_racing_event_cards")
        mssqldb.Execute("truncate table vs_horse_racing_event_cards")

        XMLDirectoryList = self.GetXMLDirectoryList(self.GetXMLCommonPath(), True)
        for XMLDirectory in XMLDirectoryList:
            XMLList = os.listdir(XMLDirectory)
            RTP = (XMLDirectory.split('\\')[-1]).split(' ')[0]

            for XMLFileName in XMLList:
                EventID, XMLData = self.ReadXMLData(XMLDirectory,XMLFileName)
                SQLValue = (EventID, RTP, XMLData)

                mysqldb.WriteToDB(self.__mysqlInsertSQL, SQLValue)
                mssqldb.WriteToDB(self.__mssqlInsertSQL, SQLValue)

    def GetAllCombinationMap(self, RacerCount=10):
        InitOdds = 0.0
        CombinationOddsMap = {}
        RacerList = list(range(1, RacerCount + 1))

        CombinationOddsMap[CombinationType.Win] = {}
        CombinationOddsMap[CombinationType.Place] = {}
        for RacerNum in itertools.permutations(RacerList, 1):
            CombinationOddsMap[CombinationType.Win][RacerNum] = InitOdds
            CombinationOddsMap[CombinationType.Place][RacerNum] = InitOdds

        CombinationOddsMap[CombinationType.Exacta] = {}
        for ExactaCombination in itertools.permutations(RacerList, 2):
            CombinationOddsMap[CombinationType.Exacta][ExactaCombination] = InitOdds

        CombinationOddsMap[CombinationType.Quinella] = {}
        for QuinellaCombination in itertools.combinations(RacerList, 2):
            CombinationOddsMap[CombinationType.Quinella][QuinellaCombination] = InitOdds

        CombinationOddsMap[CombinationType.Tierce] = {}
        for TierceCombination in itertools.permutations(RacerList, 3):
            CombinationOddsMap[CombinationType.Tierce][TierceCombination] = InitOdds

        CombinationOddsMap[CombinationType.Trio] = {}
        for TrioCombination in itertools.combinations(RacerList, 3):
            CombinationOddsMap[CombinationType.Trio][TrioCombination] = InitOdds

        return CombinationOddsMap

    def ClearOdds(self, CombinationOddsMap):
        for CombinationTypeKey, CombinationTypeValue in CombinationOddsMap.items():
            for Combination in CombinationOddsMap[CombinationTypeKey].keys():
                CombinationOddsMap[CombinationTypeKey][Combination] = 0.0

    def GetOddsFromXMLData(self, XMLData, CombinationOddsMap):
        TempList = []
        domobj = xmldom.parseString(XMLData)

        RacerElement = domobj.getElementsByTagName("racer")
        for child in RacerElement:
            RacerNum = int(child.getAttribute("Num"))
            TempList.append(RacerNum)
            Combination = tuple(TempList)
            CombinationOddsMap[CombinationType.Win][Combination] = float(child.getAttribute("Price"))
            CombinationOddsMap[CombinationType.Place][Combination] = float(child.getAttribute("Place"))
            TempList.clear()

        BetTypeElement = domobj.getElementsByTagName("BetType")
        for child in BetTypeElement:

            CombinationTypeIndex = CombinationType.Win
            BetType = child.getAttribute("Type")
            if BetType == "F/C":
                CombinationTypeIndex = CombinationType.Exacta
            elif BetType == "T/C":
                CombinationTypeIndex = CombinationType.Tierce
            elif BetType == "R F/C":
                CombinationTypeIndex = CombinationType.Quinella
            elif BetType == "R T/C":
                CombinationTypeIndex = CombinationType.Trio
            else:
                continue

            PricesString = child.getAttribute("Prices")
            if PricesString == "":
                continue

            TempList.clear()
            PricesStringList = PricesString.split(',')
            for Price in PricesStringList:
                TempList.append(float(Price))

            TempListIndex = 0
            for Combination in CombinationOddsMap[CombinationTypeIndex].keys():
                CombinationOddsMap[CombinationTypeIndex][Combination] = TempList[TempListIndex]
                TempListIndex += 1

        return CombinationOddsMap

    def GetBetInformation(self):
        MaxOddsList = []
        CombinationMap = self.GetAllCombinationMap()
        XMLDirectoryList = self.GetXMLDirectoryList(self.GetXMLCommonPath())

        Counter = 0
        for XMLDirectory in XMLDirectoryList:
            XMLList = os.listdir(XMLDirectory)
            RTP = XMLDirectory[len(self.GetXMLCommonPath()):]

            for XMLFileName in XMLList:
                EventID, XMLData = self.ReadXMLData(XMLDirectory,XMLFileName)
                CombinationMap = self.GetOddsFromXMLData(XMLData, CombinationMap)
                MaxOddsList.append(self.__hrExcel.WriteCombinationOddsAndMaxBetToEXCEL(CombinationMap, EventID))
                self.ClearOdds(CombinationMap)

            self.__hrExcel.WriteMaxOddsAndMaxBetToEXCEL(MaxOddsList, RTP)
            MaxOddsList.clear()

    def GetMaxPriceEachEventFromXML(self, XMLData):
        PriceFloatList = []
        domobj = xmldom.parseString(XMLData)

        RacerElement = domobj.getElementsByTagName("racer")
        for child in RacerElement:
            PriceFloatList.append(float(child.getAttribute("Place")))
            PriceFloatList.append(float(child.getAttribute("Price")))

        BetTypeElement = domobj.getElementsByTagName("BetType")
        for child in BetTypeElement:
            PricesString = child.getAttribute("Prices")
            if PricesString != "":
                PricesStringList = PricesString.split(',')
                for Price in PricesStringList:
                    PriceFloatList.append(float(Price))

        PriceFloatList.sort()
        MaxPrice = PriceFloatList[-1]
        return MaxPrice

    def FindMaxOddsForEachRTP(self):
        XMLDirectoryList = self.GetXMLDirectoryList(self.GetXMLCommonPath())
        RTPMaxPriceMap = {"85%" : 0.0, "90%" : 0.0, "95%" : 0.0}
        RTPMaxPriceEventIDMap = {"85%" : 0, "90%" : 0, "95%" : 0}

        for XMLDirectory in XMLDirectoryList:
            XMLList = os.listdir(XMLDirectory)
            RTP = (XMLDirectory.split('\\')[-1]).split(' ')[0]

            for XMLFileName in XMLList:
                EventID, XMLData = self.ReadXMLData(XMLDirectory,XMLFileName)
                MaxPrice = self.GetMaxPriceEachEventFromXML(XMLData)
                if RTPMaxPriceMap[RTP] < MaxPrice:
                    RTPMaxPriceMap[RTP] = MaxPrice
                    RTPMaxPriceEventIDMap[RTP] = EventID

        for rtp in RTPMaxPriceEventIDMap:
            print("%s : EventID = %s, MaxPrice = %s" % (rtp, RTPMaxPriceEventIDMap[rtp], RTPMaxPriceMap[rtp]))

    def AdjustProbWinForXML(self):
        ProbWinOffsetList = []
        CorrectTotalProbWin = 1.000000
        XMLDirectoryList = self.GetXMLDirectoryList(self.GetXMLCommonPath())

        for XMLDirectory in XMLDirectoryList:
            XMLList = os.listdir(XMLDirectory)
            for XMLFileName in XMLList:
                EventID, XMLData = self.ReadXMLData(XMLDirectory,XMLFileName)

                ProbWinList = []
                domobj = xmldom.parseString(XMLData)
                RacerElement = domobj.getElementsByTagName("racer")
                for child in RacerElement:
                    ProbWinList.append(float(child.getAttribute("ProbWin")))

                ProbWinOffsetList.append([])
                ListIndex = len(ProbWinOffsetList) - 1
                ProbWinOffsetList[ListIndex].append(int(EventID))
                ProbWinOffsetList[ListIndex].append(ProbWinList)

                TotalProbWin = float('%0.6f' % sum(ProbWinList))
                Offset = float('%0.6f' % (CorrectTotalProbWin - TotalProbWin))
                ProbWinOffsetList[ListIndex].append(TotalProbWin)
                ProbWinOffsetList[ListIndex].append(Offset)

                OldRacer10 = float('%f' % ProbWinList[len(ProbWinList) - 1])
                ProbWinList[len(ProbWinList) - 1] += Offset
                NewRacer10 = float('%0.6f' % ProbWinList[len(ProbWinList) - 1])

                #RacerElement[9].setAttribute("ProbWin", str(NewRacer10))
                #for child in RacerElement:
                #    print(child.getAttribute("ProbWin"))

                if TotalProbWin != CorrectTotalProbWin:
                    XMLData = XMLData.replace(str(OldRacer10), str(NewRacer10))
                    NewXMLDirectory = XMLDirectory.replace("Viewer1.0.3", "Viewer1.0.3_Temp")
                    fileobject = open(NewXMLDirectory + "\\" + XMLFileName, "w", encoding='utf-16')
                    fileobject.write(XMLData)
                    fileobject.close()

                ProbWinOffsetList[ListIndex].append(NewRacer10)
                NewTotalProbWin = float('%0.6f' % sum(ProbWinList))
                ProbWinOffsetList[ListIndex].append(NewTotalProbWin)

        self.__hrExcel.WriteProbWinToEXCEL(ProbWinOffsetList)