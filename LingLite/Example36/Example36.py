import sys
print(sys.version)
print('\n')


import Example_1 as E1
import Example_2 as E2

fileName = r'Naughty Brother.txt'
testFile = r'test.txt'

print(E1.Read(fileName) + '\n')

LineList = E1.ReadLine(fileName)
print(LineList)


E1.Write(testFile, 'test')