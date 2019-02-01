from IPython.display import clear_output
# have a class called cart that retains items and has methods to add, remove, and show

# step #1: create the cart class
class Cart():


    # when instantiated, cart object should define empty list for items
    def __init__(self):
        self.cart = []

    # create a method to show cart
    def showCart(self):
        print('Here is your cart:')
        for item in self.cart:
            print(self.cart)


    # create a method to add to cart
    def addItem(self):
        item = input('Type the name of an item, then hit enter to add the item to your cart.')
        self.cart.append(item)
        print('{} has been added to your cart.'.format(item))


    # create a method to remove from cart
    def removeItem(self):
        item = input('Type the name of an item, then hit enter to remove the item from your cart.')
        if item in self.cart:
            self.cart.remove(item)
            print('{} has been removed from your cart.'.format(item))
        else:
            print('item is not in cart')

    # create a method to clear output
    def clearCart(self):
        print('Your cart is empty.')
        self.cart.clear()



# create instance of cart object with empty list
webcart = Cart()


# start the while loop until user quits
while True:
    # ask for input
    # ask if they would like to add, remove, show, perform steps using cart methods

    ans = input('Welcome to our webstore! \n Type add to add to add an item to your cart. \n Type remove to' +
            ' remove an item from your cart. \n Type show to display your cart. \n Type clear to clear output \n Type quit to quit.')
     # base case
    #clear_output needs to be take place after input, else the program outputs nothingq
    clear_output()
    if ans.lower() == 'quit':
        webcart.showCart()
        break
    elif ans.lower() == 'add':
        webcart.addItem()
    elif ans.lower() == 'remove':
        webcart.removeItem()
    elif ans.lower() == 'show':
        webcart.showCart()
    elif ans.lower() == 'clear':
        webcart.clearCart()
    else:
        print('Wrong command, try again!')
