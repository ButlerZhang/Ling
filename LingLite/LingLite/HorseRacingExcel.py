#!/usr/local/bin/python

# Copyright (c) 2018
# All rights reserved.
# Describe : horse racing excel
# Author   : Butler
# Date     : 2018-08-17

import xlwt



class HorseRacingExcel(object):
    """horse racing excel tatistics"""

    def __init__(self):
        self.colWidth = 256 * 20
        self.contextStyle = self.GetContextStyle()
        self.typeStartIndex = len("CombinationType.")
        self.maxPayoutList = [10000.00, 100000.00, 1000000.00, 10000000.00]

    def GetContextStyle(self):
        contextStyle = xlwt.XFStyle()
        contextStyle.alignment = xlwt.Alignment()
        contextStyle.alignment.horz = xlwt.Alignment.HORZ_CENTER
        contextStyle.alignment.vert = xlwt.Alignment.VERT_CENTER
        return contextStyle

    def GetWorkbook(self, EventID):
        wb = xlwt.Workbook()
        ws = wb.add_sheet(str(EventID))

        ws.write(0, 0, "Combination Type", self.contextStyle)
        ws.col(0).width =  self.colWidth
        ws.write(0, 1, "Combination", self.contextStyle)
        ws.col(1).width = self.colWidth
        ws.write(0, 2, "Odds", self.contextStyle)
        ws.col(2).width = self.colWidth

        startCol = 3
        return wb, ws, startCol

    def WriteSingleRow(self, ws, row, startCol, Tip, Combination, Odds):

        ws.write(row, 0, Tip, self.contextStyle)
        ws.write(row, 1, str(Combination), self.contextStyle)
        ws.write(row, 2, Odds, self.contextStyle)

        col = startCol
        for MaxPayout in self.maxPayoutList:
            ws.write(row, col, float('%.2f' % (MaxPayout / Odds)), self.contextStyle)
            col += 1

    def WriteMinMaxOdds(self, CombinationOddsMap, TempOdds, Tip, row, startCol, ws):
        for CombinationTypeKey, CombinationTypeValue in CombinationOddsMap.items():
            for Combination, Odds in CombinationTypeValue.items():
                if TempOdds == Odds:
                    self.WriteSingleRow(ws, row, startCol, Tip + str(CombinationTypeKey)[self.typeStartIndex:], Combination, Odds)
                    return CombinationTypeKey, Combination, Odds

    def WriteCombinationOddsAndMaxBetToEXCEL(self, CombinationOddsMap, EventID):
        wb, ws, startCol = self.GetWorkbook(EventID)

        col = startCol
        for MaxPayout in self.maxPayoutList:
            ws.write(0, col, "(MaxPayout = " + str(MaxPayout) + ") / Odds", self.contextStyle)
            ws.col(col).width = 256 * 30
            col += 1

        row = 1
        MaxOdds = 0.0
        MinOdds = 9999999999.99

        for CombinationTypeKey, CombinationTypeValue in CombinationOddsMap.items():
            for Combination, Odds in CombinationTypeValue.items():
                self.WriteSingleRow(ws, row, startCol, str(CombinationTypeKey)[self.typeStartIndex:], Combination, Odds)
                row += 1

                if MaxOdds < Odds:
                    MaxOdds = Odds

                if MinOdds > Odds:
                    MinOdds = Odds

        self.WriteMinMaxOdds(CombinationOddsMap, MinOdds, "Min Odds : ", row + 2, startCol, ws)
        TempType, TempCombination, TempOdds = self.WriteMinMaxOdds(CombinationOddsMap, MaxOdds, "Max Odds : ", row + 3, startCol, ws)

        wb.save("ResultFiles\\MaxBetMaxWin\\" + str(EventID) + ".xls")
        return [EventID, TempType, TempCombination, TempOdds]

    def WriteMaxOddsAndMaxBetToEXCEL(self, MaxOddsList, RTP):
        wb = xlwt.Workbook()
        ws = wb.add_sheet("Max Bet")

        ws.write(0, 0, "Event ID", self.contextStyle)
        ws.col(0).width = self.colWidth
        ws.write(0, 1, "Combination Type", self.contextStyle)
        ws.col(1).width =  self.colWidth
        ws.write(0, 2, "Combination", self.contextStyle)
        ws.col(2).width = self.colWidth
        ws.write(0, 3, "Odds", self.contextStyle)
        ws.col(3).width = self.colWidth

        col = 4
        for MaxPayout in self.maxPayoutList:
            ws.write(0, col, "(MaxPayout = " + str(MaxPayout) + ") / Odds", self.contextStyle)
            ws.col(col).width = 256 * 30
            col += 1

        row = 1
        MaxOdds = 0.0
        MaxOddsEventList = []
        for EventList in MaxOddsList:
            ws.write(row, 0, int(EventList[0]), self.contextStyle)                         #EventID
            ws.write(row, 1, str(EventList[1])[self.typeStartIndex:], self.contextStyle)      #Type
            ws.write(row, 2, str(EventList[2]), self.contextStyle)                         #Combination
            ws.write(row, 3, EventList[3], self.contextStyle)                              #Odds

            col = 4
            for MaxPayout in self.maxPayoutList:
                ws.write(row, col, float('%.2f' % (MaxPayout / EventList[3])), self.contextStyle)
                col += 1

            if EventList[3] > MaxOdds:
                MaxOdds = EventList[3]
                MaxOddsEventList = EventList

            row += 1

        row += 2
        ws.write(row, 0, "Max Odds = ", self.contextStyle)                                #Tip
        ws.write(row, 1, int(MaxOddsEventList[0]), self.contextStyle)                     #EventID
        ws.write(row, 2, str(MaxOddsEventList[2]), self.contextStyle)                     #Combination
        ws.write(row, 3, MaxOddsEventList[3], self.contextStyle)                          #Odds

        wb.save("ResultFiles\\MaxBetMaxWin\\_" + RTP + ".xls")

    def WriteProbWinToEXCEL(self, ProbWinOffsetList):
        wb = xlwt.Workbook()
        ws = wb.add_sheet("ProbWin")
        colWidth = 256 * 15

        ws.write(0, 0, "Event ID", self.contextStyle)
        ws.col(0).width = colWidth

        for col in range(1,11):
            ws.write(0, col, "Racer" + str(col), self.contextStyle)
            ws.col(col).width =  colWidth

        ws.write(0, 11, "Total", self.contextStyle)
        ws.col(11).width =  colWidth

        ws.write(0, 12, "Offset", self.contextStyle)
        ws.col(12).width =  colWidth

        ws.write(0, 13, "New Racer10", self.contextStyle)
        ws.col(13).width =  colWidth

        ws.write(0, 14, "New Total", self.contextStyle)
        ws.col(14).width =  colWidth

        row = 1
        for EventList in ProbWinOffsetList:
            ws.write(row, 0, EventList[0], self.contextStyle)           #event id
            ws.write(row, 1, EventList[1][0], self.contextStyle)        #racer
            ws.write(row, 2, EventList[1][1], self.contextStyle)        #racer
            ws.write(row, 3, EventList[1][2], self.contextStyle)        #racer
            ws.write(row, 4, EventList[1][3], self.contextStyle)        #racer
            ws.write(row, 5, EventList[1][4], self.contextStyle)        #racer
            ws.write(row, 6, EventList[1][5], self.contextStyle)        #racer
            ws.write(row, 7, EventList[1][6], self.contextStyle)        #racer
            ws.write(row, 8, EventList[1][7], self.contextStyle)        #racer
            ws.write(row, 9, EventList[1][8], self.contextStyle)        #racer
            ws.write(row, 10, EventList[1][9], self.contextStyle)       #racer
            ws.write(row, 11, EventList[2], self.contextStyle)          #total prob win
            ws.write(row, 12, EventList[3], self.contextStyle)          #offset
            ws.write(row, 13, EventList[4], self.contextStyle)          #racer10
            ws.write(row, 14, EventList[5], self.contextStyle)          #new total prob win
            row += 1

        wb.save("ResultFiles\\ProbWin\\probwin.xls")
