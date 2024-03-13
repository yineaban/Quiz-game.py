name=input("Enter name:\n")
other_name=input("Enter your crush/ any femal you love:\n")
combined=name+other_name
t=combined.count("t")
r=combined.count("r")
u=combined.count("u")
e=combined.count("e")
true=t+r+u+e
l=combined.count("l")
o=combined.count("o")
v=combined.count("v")
e=combined.count("e")
love=l+o+v+e
true_love=str(true)+str(love)
if int(true_love) >60:
    print(f"the probablity she loves you is{true_love}% so it is better to have wedding with her")
elif int(true_love )>50:
    print(f"it good to have wedding with her,she loves you {true_love}%")  
elif int(true_love) >40:
    print(f"you can have temporary relation shhip with this person not long last{true_love}%")
elif int(true_love) <40:
    print(f"your relation should no more than one day,the perecent she loves you is {true_love}%")
else:
    print(f"you have to stope such relation ship her feeling about you is{true_love}%")
print("This magic done by yinager kinde.")




