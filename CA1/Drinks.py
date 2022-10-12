import random 

# create dictionary of drinks from text file
drinks_dict = {}
menu = []

with open('Cocktails.txt', 'r') as file:
    for line in file:
        line = line.strip()
        drink, ingredients = line.split(': ')
        ingredients = ingredients.split(', ')
        drinks_dict[drink] = ingredients
        menu.append(drink)

# create dictionary of ingredients by type
ingredients_dict = {}

with open('Ingredients.txt', 'r') as file:
    for line in file:
        line = line.strip()
        type, ingredients = line.split(': ')
        ingredients = ingredients.split(', ')
        ingredients_dict[type] = ingredients

class Drink:
    def __init__(self, drink_name) -> None:
        try:
            self.name = menu[int(drink_name)]
        except:
            self.name = drink_name.lower()

        self.ingredients = drinks_dict[self.name]
        self.spirits = []
        self.mixers = []
        self.syrups = []
        self.garnishes = []

        self.__categorise_ingredients()

    def __categorise_ingredients(self):
        for item in self.ingredients:
            if item in ingredients_dict['spirits']:
                self.spirits.append(item)
            elif item in ingredients_dict['mixers']:
                self.mixers.append(item)
            elif item in ingredients_dict['syrups']:
                self.syrups.append(item)
            elif item in ingredients_dict['garnishes']:
                self.garnishes.append(item)
            else:
                print(item, 'not found in ingredients file yet')

    def __str__(self):
        output = self.name
        output += f'\nspirits: {[item for item in self.spirits]}'
        output += f'\nmixers: {[item for item in self.mixers]}'
        output += f'\nsyrups: {[item for item in self.syrups]}'
        output += f'\ngarnishes: {[item for item in self.garnishes]}'

        return output

    def guess_ingredients(self):
        print('Drink order:', self.name)
        while not self.are_lists_empty():
            self.print_hint()
            guess = input('Guess an ingredient: ')
            self.check_ingredient_match(guess)


    def print_hint(self):
        print(f'\nHint: There are {len(self.spirits)} spirits, {len(self.mixers)} mixers, {len(self.syrups)} syrups, and {len(self.garnishes)} garnishes left to guess')

    def check_ingredient_match(self, guess):
        if guess in self.spirits:
            self.spirits.remove(guess)
        elif guess in self.mixers:
            self.mixers.remove(guess)
        elif guess in self.syrups:
            self.syrups.remove(guess)
        elif guess in self.garnishes:
            self.garnishes.remove(guess)
        else:
            print(f'{self.name} does not contain {guess}')

    def are_lists_empty(self):
        lists = [self.spirits, self.mixers, self.syrups, self.garnishes]
        for item in lists:
            if len(item) != 0:
                return False
        return True


class Order:
    def __init__(self, order_size) -> None:
        self.drinks_list = []
        self.menu_length = len(menu)
        self.order_size = order_size
        print('menu length:', self.menu_length)
        
        for i in range(self.order_size):
            n = random.randint(0, self.menu_length - 1) 
            new_drink = Drink(menu[n])
            self.drinks_list.append(new_drink)

        
        

# mydrink = Drink(1)
# print(mydrink)

# my_order = Order(4)
# for drink in my_order.drinks_list:
#     print(drink, '\n')

for i in range(6):
    print(Drink(i).guess_ingredients(), '\n')