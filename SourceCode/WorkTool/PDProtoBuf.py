#!/usr/local/bin/python



class PDProtoBuf(object):
    """format protobuf message for read"""

    def __init__(self):
        self.__fileCount = 1
        self.__resultFileName = ""

    def AnalyzeLogFie(self, fileName):
        #targtMap = {"ContextData{": self.FormatData, "CommandData{": self.FormatData}
        targetList = ["ContextData{", "CommandData{"]

        with open(fileName, 'r') as fileHandler:
            for line in fileHandler.readlines():

                for target in targetList:
                    startIndex = line.find(target)

                    if startIndex >= 0:
                        line = line[startIndex:]
                        self.FormatData(line, target)

    def FormatData(self, fileData, dataType):
        word = ""
        dataList = []

        for ch in fileData:
            if ch == '{':
                dataList.append(word)
                dataList.append('{')
                word = ""

            elif ch == '}':
                if len(word) > 0:
                    if word.find('=') >= 0:
                        dataList.append(word + ',')
                    else :
                        dataList[len(dataList)-1] += word
                    word = ""
                dataList.append('}')
                word = ""

            elif ch == '[':
                word += ch

            elif ch == ']':
                if len(word) == 0:
                    dataList[len(dataList)-1] += ch
                else:
                    dataList.append(word + ']')
                    word = ""

            elif ch == ',':
                if len(word) == 0:
                    dataList[len(dataList)-1] += ch
                elif word.find('=') < 0:
                    dataList[len(dataList)-1] += word + ch
                    word = ""
                elif word.find('[') < 0 or word.find('@') > 0:
                    dataList.append(word + ',')
                    word = ""
                else:
                    word += ch

            elif ch != '\n':
                if ch != ' ' or len(word) > 0:
                    word += ch

            #debug
            #for data in dataList:
            #    if data.find("powerCrapsChipsAmount") >= 0:
            #        print("I come here")

        fileName = str(self.__fileCount) + dataType[:len(dataType)-1] + ".txt"
        self.WriteList(fileName, dataList)
        self.__fileCount += 1

    def WriteList(self, fileName, dataList):
        tabString =""
        with open(fileName, 'w') as fileHandler:
            for data in dataList:

                if data.find('}') >=0 :
                    tabString = tabString[0: len(tabString)-1]

                print(tabString + data)
                fileHandler.write(tabString + data + "\n")

                if data == '{':
                    tabString += "\t"

if __name__ == '__main__':
    print("start ...")
    PDProtoBuf().AnalyzeLogFie("AspectGaming.log")
    print('\nProgram executed completed!\n')
