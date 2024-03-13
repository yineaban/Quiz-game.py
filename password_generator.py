import random
letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Symbols=[",","/",".","*","!","?","&","$","%","@"]
number=["1","2","3","4","5","6","7","8","9","0"]
password=""

    # how many letters ,symbols and numbers you want to use
    # passored assign
    # write way and 
letter_needed=input("how many letters do you want to use?\n")
  
symbol_needed=input("how many symbols do you want to use?\n")
number_needed=input("how many numbers do you want to use?\n")
password=[]
for n in range(0,int(letter_needed)):
    
    
    password.append(random.choice(letter))
for k in range(0,int(symbol_needed)):

    password.append(random.choice(Symbols))
for b in range(0,int(number_needed)):
   password.append(random.choice(number))
   random.shuffle(password)
  
pass_word=""
for p in password:
    pass_word+=p

print("yine this is the password you have generayted\n",pass_word)
