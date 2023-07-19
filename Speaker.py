import os
import pyttsx3

if __name__ == "__main__":
    print("Welcome to Hariom's Speaker")
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1.2)
    while True:
        x = input("Start conversation ")
        if x == "q":
            print("quit")
            engine.say('thankyou for using Harioms speaker')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
