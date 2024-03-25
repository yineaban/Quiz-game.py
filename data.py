# data=[{
#     "name":"instagram",
#     "follower_count":346,
#   "description":"social media platform",
#   "country":"united states"
      
    
# },
#       {
#     "name":"cristiano ronaldo",
#     "follower_count":215,
#   "description":"foot baller",
#   "country":"portugal"
      
    
# },
#       {
#     "name":"ariana grand",
#     "follower_count":183,
#   "description":"musician and actress",
#   "country":"united states"
      
    
# },
# {
#     "name":"dwane jhonson",
#     "follower_count":181,
#   "description":"acter and proffessional wrestler",
#   "country":"united states"
      
    
# },
# {
#     "name":"hayat nasser",
#     "follower_count":2,
#   "description":"tiktoker",
#   "country":"Ethiopia"
      
    
# },
# {
#     "name":"shakira",
#     "follower_count":45,
#      "description":"musician",
#   "country":"colombia"
      
    
# },
# {
#     "name":"rihana",
#     "follower_count":146,
#   "description":"musician",
#   "country":"alabana"
      
    
# }

# ]
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18

        },
        "cost": 2.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24

        },
        "cost": 2.5
    },
   "capccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3
    }

}
"""i will think more about it"""
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

is_on=True
def is_resourece_sufficient(order_ingredient):
    
    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"insufficient resources of {item}")
            return False
    return True

def process_coins():
    print("how many coins do you want")
    total=int(input("how many quarters of coin you want"))*0.25
    total+=int(input("how many dimes of coin you want"))*0.1
    
    
    total+= int(input("how many nickels of coin you want")) * 0.05
    total+= int(input("how many  pennis of coin you want") )* 0.01
    return total
def is_transaction_successful(money_recieved,drink_cost):
    global profit
#     true when payment is accepted and false when it is insufficient

    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"the change in transaction is {change}")
        profit+=drink_cost+change
        return True
    else:
        print(f"it is not enougn money ,{drink_cost-money_recieved}should refunded")
        return False


def make_coffe(drink_name,order_ingredients):
    """ deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your drink {drink_name} Enjoy")







while is_on:
    choice=input("what would you like (espreso latte or capccino ?")
    if choice=="off":
        is_on=False
    elif choice=="report" :
        print(f" water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print( f"money:{profit}")
    else:
        drink=menu[choice]
        
        
        y=is_resourece_sufficient(drink["ingredients"])
     
        if y:
             
            
            payment=process_coins()
           
           

            if is_transaction_successful(payment,drink["cost"]):
                x=make_coffe(choice,drink["ingredients"])
              











