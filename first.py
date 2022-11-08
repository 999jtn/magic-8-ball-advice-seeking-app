import random
import sys
import time

#Variables
i = "root"
j = "damn bruhhh"
k = 1
nammee = ""

# Advice Choices
oho = [
        "It is certain", "Outlook good", "You may rely on it, but carefully.",
        "Oho, My sources got tensed. Ask again later", "Yes", "Most likely", "Concentrate and ask again, you are acting weird.",
        "I think you should do.", "Could be", "My reply is no, this is not the way we treat.",
        "My sources say no, you must consult someone real on this.",
        "Not so sure", "42", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
        "Negative", "Unclear, ask again", " No", "Possible, but not probable"
        ]

    
def think():
    time.sleep(2)
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


while i.__contains__("y") or i == "root" or i == "y" and i != "n":
    if i == "root":
        nammee = input("\nHey, What's You Name bruhh? : ")
        
    print("\nWhat advice do you want, ask me your question? ")
    ques = input("QUESTION : ")
    
    if len(ques) > 20: 
        print("Let me dig into the life of ocean to search for your answer.")
        think()
    elif len(ques) < 7:
        print("NOTE : Too short question. You tryna fool me, huhhh!")
        time.sleep(1)
        print("No advice for now!")
        exit()
    elif ques == "":
        print("ADVICE : [EMPTY SPACE]")
        think()
        print("Same PINCH")
        exit():  
        
    print("Hmmmmmm.....")
    think()
    
    print("\rADVICE : " + random.choice(oho))
    
    time.sleep(3)
     
    i = input("\nWant some other advice (Yes/No) : ").casefold()
    print("")
    
print("Have a Nice Day!, " + str(nammee))
print("")
    