import sys
print(sys.version)
print('\n')

g_sourceFileName = r"DataSource//Naughty Brother.txt"
g_resultFileName1 = r"ResultFiles//result1.txt"
g_resultFileName2 = r"ResultFiles//result2.txt"

import Example8_TCPServer as E8

E8.TCPServer()
