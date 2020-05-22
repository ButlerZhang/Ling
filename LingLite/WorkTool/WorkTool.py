#!/usr/local/bin/python

import PDProtoBuf


if __name__ == '__main__':

    FileData = '''ContextData{state=5, gameState=15, language=en-US, theme=null, paytable=Field2To1, denomination=1, 
    selectedBonus=0, selections=110, betMultiplier=1, cash=0, credits=0, totalBet=1, extraBet=0, totalWin=0,
    baseGameTotalWin=0, freeGameTotalWin=0, progressiveTotalWin=0, bonusTotalWin=0, gambleTotalWin=0, gamesSinceLastFeature=-1,
    numFreeSpinsTotalWon=0, numFreeSpinsRemaining=0, messages=[Out Of Service, Power Reset, Unlicensed Mode, Show Only Mode],
    moneyRelatedMessages=null, autoplay=false, testMode=false, freeGameMode=false, specialGameMode=false,
    loggedIn=false, winLossHistory=[B@24954e82, screenButtonStates=[B@5b1f5fcc, activeBonusType=-1, win=0, mathParams=[],
    result=ResultData{stops=[I@642f324d, stopsIndices=null, numFreeSpinsWon=0, specialMask=0, scatterMask=0, scatterWin=0,
    scatterMultiplier=0, paylineMask=[I@4a29fe2e, paylineWin=[I@79135a38, paylineMultiplier=[I@77fceac6}, multipleResults=null,
    gamble=null, bonusPick=null, progressive=null, cashableCents=0, nonRestrictedCents=0, restrictedCents=0, maxBet=200,
    stateLongData=0, stateStringData=null, buttonPanel=ButtonPanelData{panelName=Default,
    buttons=[ButtonData{name=A, value=0, type=Cashout, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=B, value=0, type=Disabled, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=C, value=0, type=Disabled, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=D, value=0, type=Disabled, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=E, value=0, type=Disabled, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=F, value=0, type=Disabled, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=G, value=0, type=Attendant, enabled=true, startPlay=false, backgroundImage=},
    ButtonData{name=H, value=1, type=Multiplier, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=I, value=3, type=Multiplier, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=J, value=5, type=Multiplier, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=K, value=10, type=Multiplier, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=L, value=20, type=Multiplier, enabled=false, startPlay=false, backgroundImage=},
    ButtonData{name=M, value=0, type=Play, enabled=false, startPlay=false, backgroundImage=}]},
    powerCrapsMinBet=10, powerCrapsMaxBet=1000, powerCrapsOdds=2, powerCrapsChipsAmount=10,20,50,100,500,1000}'''

    PDProtoBuf.PDProtoBuf().ContextDataFormat(FileData)
    print('\nProgram executed completed!\n')
