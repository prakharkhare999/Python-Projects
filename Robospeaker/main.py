'''
this code for mac
import os
if __name__ == '__main__':
    print("welcome to Robospeaker 1.1 created by Prakhar")
    while (True):

     x = input("Enter what you want to speak: ")
     if x == "q":
         os.system("say 'bye bye friend' ")
         break
     command = f"powershall {x}"
     os.system(command)
     '''
import os
import win32com.client as wincl

if __name__ == '__main__':
    print("welcome to Robospeaker 1.1 created by Prakhar")
    speaker = wincl.Dispatch("SAPI.SpVoice")
    while (True):
        x = input("Enter what you want to speak: ")
        if x == "q":
            speaker.Speak('bye bye friend')
            break
        speaker.Speak(x)
