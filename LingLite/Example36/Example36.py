import sys
print(sys.version)
print('\n')

sourceFileName = r"Naughty Brother.txt"
resultFileName1 = r"ResultFiles//result1.txt"
resultFileName2 = r"ResultFiles//result2.txt"


import Example_3 as E3

E3.Dumps(sourceFileName, resultFileName1)

E3.Dump("hello", resultFileName2)

print(E3.Load(resultFileName1))
print(E3.Load(resultFileName2))