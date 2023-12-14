
#Creating class
class Menu:
    def __init__(self, category, name, portion, price):
        self.category = category
        self.name = name
        self.portion = portion
        self.price = price
    
    # Creating methods
    def set_category(self, category):
        self.category = category
    
    def set_name(self, name):
        self.name = name
    
    def set_portion(self, portion):
        self.portion = portion
    
    def set_price(self, price):
        self.price = price

    def get_category(self):
        return self.category

    def get_name(self):
        return self.name
    
    def get_portion(self):
        return self.portion
    
    def get_price(self):
        return self.price


# Creating a main function
def main():


    menu_list = menu()


    #category list that contains what is selected by the user
    selected_category_list = []
    #category name that contains what is selected by the user
    selected_name_list = []
    #portion  list that contains what is selected by the user
    selected_portion_list = []
    #it will append prices that depends on the selection of category, name and portion by the user
    prices_list = []

    while True:
        # Creating instance of Menu class
        order_of_user = Menu(' ', ' ', ' ', " ")

        
        category = create_category(menu_list) #function takes menu_list and returns category list
        order_of_user.set_category(select_category(category))
        selected_category_list.append(order_of_user.get_category())

        name_list = create_food_names(menu_list, order_of_user.get_category()) # function takes menu_list and returns category name list
        order_of_user.set_name(select_food_names(name_list, order_of_user.get_category()))
        selected_name_list.append(order_of_user.get_name())


        portion_list = create_portion(menu_list, order_of_user.get_category(), order_of_user.get_name()) # function takes menu_list and returns portion list
        order_of_user.set_portion(select_portion(portion_list, order_of_user.get_name()))
        selected_portion_list.append(order_of_user.get_portion())

        
        for i in menu_list:
            #here we get rid of $ sign so we can add the prices as floats into price list
            order_of_user.set_price(float(i[-1][1:]))
            if i[0] == order_of_user.get_category() and i[1] == order_of_user.get_name() and i[2] == order_of_user.get_portion():
                prices_list.append(order_of_user.get_price() )
            

        # Add New item and Checkout
        print('1. Add New \n2. Checkout')
        print()
        choice = input('Please select an operation: ')

# if user enters numbers other than 1 or 2 the program will stop
        if choice == '1':
            continue
        elif choice == '2':
            for i in range(len(selected_category_list)):
                # 40 and 21 here are random numbers in order to make the output look more nicer
                print(selected_name_list[i] + (40-(len(selected_name_list[i])))*" " + selected_portion_list[i] + (21-len(portion_list))*" " + "$" + str(prices_list[i]))
            
            print()
            total = format(sum(prices_list) , '.2f')
            print('-------------------------------------------------------------------------------')
            print()
            print("Total price: " + 50*" " + "$" + str(total))
            break

        else:
            print('Error! Operation undefined!')
            break


#creating all items' list seperately and deleting the first line of 'menu.txt'
def menu():
    filename = open('menu.txt', 'r')
    menu_list = []

    
    line = filename.readline().rstrip()
    while line != '':
        #deleting ; from each line of 'menu.txt'
        menu_list.append(line.split('; '))
        line = filename.readline().rstrip()
    # deleting the first line in 'menu.txt'
    del menu_list[0]
    filename.close()
    return menu_list


# Creating category list
def create_category(menu_list):
    category_list = []
    
    for item in menu_list:
        category = item[0]
        
        if category not in category_list:
            category_list.append(category)

    return category_list


# The selection of category which contains the category list
def select_category(category_list):
    while True:
        print('Product Categories')
        for i in range(len(category_list)):
        #displays all the elements from category list as menu's categories
            print(f'{i+1}. {category_list[i]}')
        
        choice = input("Please select product category: ")
        print()
        try:
            choice = int(choice)
        except ValueError:
            print()
            print('ERROR! Decimals and alphabetic character are not allowed!')
            print('-------------------------------------------------------------')

        else:
            if not(1 <= choice <= len(category_list)):
                print()
                print("Error! Please enter a valid choice")
                print('-------------------------------------------------------------')

            else:
                category = category_list[choice-1]
                return category


#creating name lists
def create_food_names(menu_list, category):
    name_list = []

    for item in menu_list:
        name = item[1]

        if (item[0] == category) and name not in name_list:
            name_list.append(name)

    return name_list



#process of selecting names of the food that user wants
def select_food_names(name_list, category):

    while True:
        print('Products in', category)
        for i in range(len(name_list)):
        #displays all the elements from names list as category names
            print(f'{i+1}. {name_list[i]}')
        
        choice = input("Please select product category: ")
        print()
        try:
            choice = int(choice)
        except ValueError:
            print()
            print('ERROR! Decimals and alphabetic character are not allowed!')
            print('-------------------------------------------------------------')

        else:
            if not(1 <= choice <= len(name_list)):
                print()
                print("Error! Please enter a valid choice")
                print('-------------------------------------------------------------')

            else:
                name = name_list[choice-1]
                return name




# portion list
def create_portion(menu_list, category, name):
    portion_list = []
    for i in menu_list:
        portion = i[2]
        if (i[0] == category and i[1] == name) and portion not in portion_list:
            portion_list.append(portion)
    
    return portion_list


#process of selecting portions
def select_portion(portion_list, name):

    while True:
        print(name, 'Portions')
        for i in range(len(portion_list)):
        #Displays all the elements from portions list as portions
            print(f'{i+1}. {portion_list[i]}')
        

        # User must only enter integers
        choice = input("Please select product category: ")
        print()
        try:
            choice = int(choice)
        except ValueError:
            print()
            print('ERROR! Decimals and alphabetic character are not allowed!')
            print('-------------------------------------------------------------')

        else:
            if not(1 <= choice <= len(portion_list)):
                print()
                print("Error! Please enter a valid choice")
                print('-------------------------------------------------------------')


            else:
                portion = portion_list[choice-1]
                return portion

main()