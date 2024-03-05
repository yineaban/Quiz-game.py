import random
computer_wins=0
user_wins=0
options=["rock","scisor","paper"]
while True:
    user=input("enter rock/scisor/paper q to quit").lower()
    if user=="q":
        break
    if user not in options:
        continue
    random_number=random.randint(1,2)
    computer_pick=options[random_number]
    print("computer picked",computer_pick)
    if user=="rock" and computer_pick=="scisor":
        print("you won")
        user_wins=+1
    elif user=="paper" and computer_pick=="scisor":
        print("you won")
        user_wins=+1
    elif user=="scisor" and computer_pick=="rock":
        print("you won")
        user_wins=+1
    else:
        print("you lost!")
        computer_wins+=1
        
print("you have won ",user_wins,"times")
print("you have lost ",computer_wins,"times")
print("good bye!")

    
    
    
