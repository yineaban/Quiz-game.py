import random
top_range=input("Enter anumber:")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range <=0:
      print("please Enter the next larger than 0 number:")
      quit()
else:
    print("please Enter the next larger number:")
    quit()
    

r=random.randint(0,top_range)
print(r)
number_of_guess=0
while True:
    number_of_guess+=1
    guess=input("Enter your guess")
    if guess.isdigit():
        guess=int(guess)
    else:
     print("anumber for next time")
     continue
    if guess==r:
        print("congra you got it!")
        break
    else:
        if guess>r:
            print("you guessed above the number")
        else:
            print("you guessed below the number")
        
        
print("you have got the guess",guess,"nnuber of guesses")

        
    