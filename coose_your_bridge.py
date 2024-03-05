# coose your bridge adventure:
name=input("enter your name:")
print("welcome ",name,"to this adventure!")
answer=input("you are on dirt road ,it has come to an end and you can go left and right(left/right)")
if answer=="left":
    answer=input("you come to ariver,you can walk around it or swim across it?type to walk aorund and swim to swim across(swim/walk)")
    if answer=="swim":
        print("you swam and eaten by alligators")
    elif answer=="walk":
      print("you walked for many miles,ran out of water and you lost the game!")
    else:
      print("invalid option")
elif answer=="right":
    answer=input("you come to bridge it looks whobbly,do you want to cross it or walkback?(cross/back)")
    if answer=="back":
        print("you go back to the main road now you can to decide to drive to the left or to the right")
    elif answer=="cross":
        answer=input("when you cross you 'll get the strange do you meet or not(yes/no)")
        if answer=="yes":
            print("you talk to strange and the gave you gold,you won!")
        if answer=="no":
            print("you ignore the stranges and you lose!")
        else:
            print("invalid option")
    else:
      print("invalid option!")
else:
    print("invalid option!")
            
        
      
   
    
    
    
             
             
             
             
             
             
             
             
