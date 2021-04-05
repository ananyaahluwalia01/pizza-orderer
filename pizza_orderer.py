#This is the first function which asks for the customer's details.
def find_details():
    #This is the local variable for a customer's name, found using 'input'.
    cust_name = input("What is your name? ").title()
    #This is the local variable that checks whether the customer wants to pick up their pizza or have it delivered.
    pick_deliver = input("Type '1' if you want to pick up your order, or '2' if you want it delivered: ").strip()
    #This checks if the input is valid or not. If it isn't valid, this loop forces the user to input a valid answer.
    while pick_deliver not in ['1', '2']:
        print("Sorry that isn't a valid option. ")
        pick_deliver = input("Type '1' if you want to pick up your order, or '2' if you want it delivered: ")
    #If the customer wants to pick up their pizza, then their address isn't required
    if pick_deliver == '1':
        cust_address = "not required"
    #If the customer wants their pizza delivered, then ask for their address and phone number
    elif pick_deliver == '2':
        cust_address = input("What is your address {}? ".format(cust_name))
        input("What is your phone number? ")
        print("Your pizza(s) will be sent to {} when you have placed your order".format(cust_address))
    #return
    return cust_name, cust_address

#This is the second function which shows the customer a menu and takes the customer's actual order. For this we use the parameter of the global variable 'name', so that we can personalise the program and refer to the customer using their inputted name.
def take_order(name):
    #This holds all the pizzas that we serve in a list.
    pizza_options = ["0", "Herbivore Food Pizza", "Semi-Solid & Stretchy Milk Pizza", "State in US-n Pizza", "Liquid Red Fruit and Green Leaves Pizza", "Dead Animal Appriciaters Pizza", "Red Flat Circle Pizza", "Rhymes with Mausage Pizza", "Pig Meat and Semi-Solid Milk Pizza", "Royal Sliced Pizza", "Small Oval Fruit Pizza", "Fish Pizza", "Sweet Course Pizza"]
    #This holds the prices of those pizzas in it's own list.
    pizza_costs = [0, 8, 6, 10, 7, 14, 15, 9, 7, 6, 10, 12, 13]
    #This function zips the list of pizzas with the list of prices into a dictionary according to order. This makes up our menu.
    pizza_menu = dict(zip(pizza_options, pizza_costs))
    #This will eventually hold the customer's order, but to start off it's an empty list, to which we will, later, append pizzas.
    cust_order = []
    print("Ok {} Here is our menu, we have a variety of Pizzas you can order from.".format(name))
    #This is the while loop in which they will be able to input whichever pizzas they want from the menu. Since the maximum amount of pizzas they are allowed is 5, the len(cust_order) checks how long the order list is, and whenever it is less than 5, it will execute the loop.
    while len(cust_order) < 5:
        #This diplays all the pizzas that we serve, and each correlates to a number, which they can type in to append that pizza to their list.
        pizza_wanted = input("""Choose a pizza by entering the number that correlates with it:
          Herbivore Food Pizza: Type '1'
          Semi-Solid & Stretchy Milk Pizza: Type '2'
          State in US-n Pizza: Type '3'
          Liquid Red Fruit and Green Leaves Pizza: Type '4'
          Dead Animal Appriciaters Pizza: Type '5'
          Red Flat Circle Pizza: Type '6'
          Rhymes with Mausage Pizza: Type '7'
          Pig Meat and Semi-Solid Milk Pizza: Type '8'
          Royal Sliced Pizza: Type '9'
          Small Oval Fruit Pizza: Type '10'
          Fish Pizz: Type '11'
          Sweet Course Pizza: Type '12'
          Or Type 'e' to end and proceed to checkout,
          You can have a maximum of 5 Pizzas in your order, type in a number, one at a time: """).lower().strip()
        #This checks whether the input is a valid one, and while it is not, it forces the customer to input a valid answer.
        while pizza_wanted not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'e']:
            print("Sorry {}, that wasn't a valid option, please pick a pizza from the menu".format(name))
            break
        #This checks whether the customer wants to exit with less than the maximum of 5, and allows them to break out of the while loop with the existing amount of pizzas they do have.
        if pizza_wanted == 'e':
            break
        #This checks if the customer put in one of the pizza options
        elif pizza_wanted in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:               
            #This line of code converts all string results into integer values that can be implemented in my code
            pizza_wanted = int(pizza_wanted)
            #This adds the pizza they want to their order, using the string number they entered, now converted into an integer, used as an index number to locate the pizza in it's position on the pizza_options list
            cust_order.append(pizza_options[pizza_wanted])
            #This displays the costumer's order for them, each pizza on a new line.
            print("Your order is: ")
            for pizza in cust_order:
                print(pizza)
            #Whenever the length of the customer's order list is less than 5, it prints the prompt "want another pizza" so that they know that 
            while len(cust_order) < 5:
                print("Want another pizza?")
                break
    return cust_order, pizza_menu

#This is the third function, where we compile all the costs of their order, and tell the customer, aka, the checkout. For it we use name, order, menu and address as parametres, for the function to properly function.
def checkout(name, order, menu, address):
    print("Here is your receipt {}: ".format(name))
    total_cost = 0
    #This prints out the customer's receipt for them, showing them everything that they ordered and the prices
    for pizza in order:
        total_cost = total_cost + menu[pizza]
        #This prints out the cost of each pizza to 2dp, since that's what prices are usually rounded to
        print("{}: ${:.2f}".format(pizza, menu[pizza]))
    DELIVERY = 3
    #This checks if the costumer wanted their pizza dilevered or wanted to pick it up, and if they wanted it delivered, it adds the constant cost of delivery ($3) to their total cost/
    if address != "not required":
        print("Delivery: ${:.2f}".format(DELIVERY))
        total_cost = total_cost + DELIVERY
    #This calculates their total cost, to 2dp as well
    print("Your total comes to: ${:.2f}".format(total_cost))

#This is the final function which finalises the customer's order, and allows them to cancel if they want to.
def cancel_order(address):
    #This is the input which gives the customer the option to either cancel their whole order and restart, or to finish off and confirm their order.
    cancel = input("If you would like to cancel your order: Type 'c', otherwise, Type 'd': ").lower().strip()
    #Checks to see whether what they inputted is actually valid, if not forces them to give a valid answer.
    while cancel not in ["c", "d"]:
        cancel = input("That was not valid. If you would like to cancel your order: Type 'c', otherwise, Type 'd': ").lower().strip()
    #Cancels order, restarting to take the next order
    if cancel == "c":
        #cancel
        print("Your order has been cancelled")
    #Confirms order, and informs the customer when and where they can pick up/recieve their order.
    elif cancel == "d":
        if address == "not required":
            print("Your order will be ready to pick up in 20 minutes")
        elif address != "not required":
            print("Your order will be delivered to your address: '{}', in around 30 minutes".format(address))
        

#This is the main program
main_program = "go"
#Keeps program running on a loop, always ready for the next order.
while main_program == "go":
    #Welcomes user to the Pizza Orderer
    print("Hi there! Welcome to the Pizza Orderer")
    #Goes to function 1 to collect all the user's details, and converts local variables like cust_name and cust_address to global ones (name, address) so they can be used in other functions.
    name, address = find_details()
    #Goes to function 2 to collect all the user's order, and converts local variables like cust_order and pizza_menu to global ones (order, menu) so they can be used in other functions.
    order, menu = take_order(name)
    #Goes to function 3 and works out cost of total order
    checkout(name, order, menu, address)
    #Confirms or cancels the whole order.
    cancel_order(address)


