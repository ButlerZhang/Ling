#import urllib.request
#file = urllib.request.urlopen("http://helloworldbook.com/data/message.txt")
#message = file.read()
#print(message)

#import easygui
#flavor = easygui.buttonbox("What is your favorite ice cream flavor?",choices = ['Vanilla', 'Chocolate', 'Strawberry'])
#flavor = easygui.choicebox("What is your favorite ice cream flavor?",choices = ['Vanilla', 'Chocolate', 'Strawberry'])
#easygui.msgbox("You picked "+ flavor)

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?", default = "Vanilla")
easygui.msgbox("You entered " + flavor)
