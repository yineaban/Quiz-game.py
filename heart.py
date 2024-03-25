for raw in range(6):
    for col in range(7):
        if (raw==0 and col%3!=0) or (raw==1 and col%3==0)or(raw-col==2) or (raw+col==8):
            print("*",end="")
            
        else:
            print(end=" ")
            
    print()
