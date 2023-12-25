import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 0.1. Created by Shafaq")
    while True:
        command = pyttsx3.init()
        x = input("Enter what you want to say: ")
        if x == 'q':
            break
        command.say(x)
        command.runAndWait()

    
