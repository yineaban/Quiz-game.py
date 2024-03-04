print("well come to my computer quiz")
play=input("do you want to play? ")
if play!="yes":
    quit()
print("let us play")
score=0
answer=input("what cpu stands for? ")
if answer=="central processing unit":
    print("correct")
    score+=1
    
else:
    print("Incorrect")
    
answer=input("what psu stands for? ")
if answer=="power supply unit":
    print("correct")
    score+=1
    
    
else:
    print("Incorrect")
answer=input("what RAM stands for? ")
if answer=="random access memory":
    print("correct")
    score+=1
    
    
else:
    print("Incorrect")
answer=input("what Rom stands for? ")
if answer=="read only memory":
    print("correct")
    score+=1
    
    
else:
    print("Incorrect")
print("you have got total score of",score)
