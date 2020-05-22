#!/usr/local/bin/python



class PDProtoBuf(object):
    """format protobuf message for read"""

    def WriteList(self, FileName, DataList):
        TabString =""
        with open(FileName, 'w') as fileHandler:
            for data in DataList:

                if data.find('}') >=0 :
                    TabString = TabString[0: len(TabString)-1]

                print(TabString + data)
                fileHandler.write(TabString + data + "\n")

                if data == "{":
                    TabString += "\t"

    def ContextDataFormat(self, FileData):
        Word = ""
        DataList = []

        for ch in FileData:
            if ch == '{':
                DataList.append(Word)
                DataList.append("{")
                Word = ""

            elif ch == '}':
                if len(Word) > 0:
                    DataList[len(DataList)-1] += Word
                    Word = ""
                DataList.append("}")
                Word = ""

            elif ch == '[':
                Word += ch

            elif ch == ']':
                if len(Word) == 0:
                    DataList[len(DataList)-1] += ch
                else:
                    DataList.append(Word + "]")
                    Word = ""

            elif ch == ',':
                if len(Word) == 0:
                    DataList[len(DataList)-1] += ch
                elif Word.find('=') < 0:
                    DataList[len(DataList)-1] += Word + ch
                    Word = ""
                elif Word.find('[') < 0 or Word.find('@') > 0:
                    DataList.append(Word + ",")
                    Word = ""
                else:
                    Word += ch

            elif ch != '\n':
                if ch != ' ' or len(Word) > 0:
                    Word += ch

        self.WriteList("result.txt", DataList)
