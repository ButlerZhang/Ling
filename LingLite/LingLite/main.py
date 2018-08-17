#!/usr/local/bin/python

# Copyright (c) 2018
# All rights reserved.
# Describe : main
# Author   : Butler
# Date     : 2018-08-17

import HorseRacing as HR



if __name__ == '__main__':

    horseracing = HR.HorseRacing()
    #horseracing.WriteXMLToDB()
    #horseracing.FindMaxOddsForEachRTP()
    #horseracing.GetBetInformation()
    horseracing.AdjustProbWinForXML()

    print('\nProgram executed completed!\n')
