def add(a,b):
    return a+b
def multt(a,b):
    return a*b
def div(a,b):
    return a/b
def sub(a,b):
    return a-b
operations={
    "+":add,
    "*":multt,
    "/":div,
    "-":sub
    
    
}
a=int(input("Enter the 1st number:"))
    
for symbol in operations:
    operator=input("Enter the operator:")
b=int(input("Enter the 2nd number:"))
cal_operation=operations[operator]
dude=cal_operation(a,b)
print(dude)
