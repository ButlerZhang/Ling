#!/usr/local/bin/python

import os
import PDProtoBuf


if __name__ == '__main__':
    PDProtoBuf.PDProtoBuf().AnalyzeLogFie("AspectGaming.log")
    print('\nProgram executed completed!\n')
    os.system('pause')
