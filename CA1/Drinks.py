import random
from typing import ClassVar

def parse_file(filename):
    '''
    read information from file, split up by colons and commmas
    eg drinkname: ingredient1, ingredient2, ingredient3...
    '''
    return_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            key, values = line.split(': ')
            values = values.split(', ')
            return_dict[key] = values

    return return_dict

# create recipe dictionaries
cocktails_recipes = parse_file('Cocktails.txt')
shots_recipes = parse_file('Shots.txt')

# create dictionary of ingredients by type
ingredients_dict = parse_file('Ingredients.txt')

menu = list(cocktails_recipes.keys()) + list(shots_recipes.keys())

def print_all_ingredients():
    for key in ingredients_dict:

        print(f'\n{key}: \t', ingredients_dict[key])


class Drink:
    __drink_name: ClassVar[str]
    __drink_type: ClassVar[str]
    __ingredients: ClassVar[list]
    # __spirits: ClassVar[list]
    # __mixers: ClassVar[list]
    # __syrups: ClassVar[list]
    # __garnishes: ClassVar[list]




    def __init__(self, drink_name, drink_type, *args:str, **kwargs:str) -> None:
        self.__drink_name = drink_name.lower()
        

        if drink_type == 'cocktail':
            self.__ingredients = cocktails_recipes[self.drink_name]
        elif drink_type == 'shot':
            self.__ingredients = shots_recipes[self.drink_name]

        # self.__categorise_ingredients()

    # def __categorise_ingredients(self):
    #     for item in self.__ingredients:
    #         if item in ingredients_dict['spirits']:
    #             self.spirits.append(item)
    #         elif item in ingredients_dict['mixers']:
    #             self.mixers.append(item)
    #         elif item in ingredients_dict['syrups']:
    #             self.syrups.append(item)
    #         elif item in ingredients_dict['garnishes']:
    #             self.garnishes.append(item)
    #         else:
    #             print(item, 'not found in ingredients file yet')

    def __str__(self):
        output = self.__drink_name
        # output += f'\nspirits: {[item for item in self.spirits]}'
        # output += f'\nmixers: {[item for item in self.mixers]}'
        # output += f'\nsyrups: {[item for item in self.syrups]}'
        # output += f'\ngarnishes: {[item for item in self.garnishes]}'

        return output

    # def guess_ingredients(self):
    #     print('Drink order:', self.name)
    #     while not self.are_lists_empty():
    #         self.print_hint()
    #         guess = input('Guess an ingredient: ')
    #         self.check_ingredient_match(guess)


    # def print_hint(self):
    #     print(f'\nHint: There are {len(self.spirits)} spirits, {len(self.mixers)} mixers, {len(self.syrups)} syrups, and {len(self.garnishes)} garnishes left to guess')

    # def check_ingredient_match(self, guess):
    #     if guess in self.spirits:
    #         self.spirits.remove(guess)
    #     elif guess in self.mixers:
    #         self.mixers.remove(guess)
    #     elif guess in self.syrups:
    #         self.syrups.remove(guess)
    #     elif guess in self.garnishes:
    #         self.garnishes.remove(guess)
    #     else:
    #         print(f'{self.name} does not contain {guess}')
    #         return
        
    #     print("Correct!", end='')

    # def are_lists_empty(self):
    #     lists = [self.spirits, self.mixers, self.syrups, self.garnishes]
    #     for item in lists:
    #         if len(item) != 0:
    #             return False
    #     return True

    def add_ingredient(self, ingredient):
        if ingredient in self.__ingredients:
            self.__ingredients.remove(ingredient)
            print("Good choice, {ingredient} has now been added")
        else:
            print(f"The customer tells you that there's no {ingredient} in a {self.__drink_name}. You quickly knock back the {ingredient} to hide your shame.")

    def add_whipped_cream(self):
        successful = bool(random.randint(0, 1))
        if successful:
            print("Odd choice, but the customer loves it! Bonus points!")
        else:
            print("The customer is lactose intolerant and afraid. Minus points.")



class Cocktail(Drink):
    def __init__(self, drink_name, drink_type, *args: str, **kwargs: str) -> None:
        super().__init__(drink_name, drink_type, *args, **kwargs)

    def shake(self):
        print('The customer was impressed by your shaking skills, bonus points!')

    def add_ice(self):
        print('Ice added successfully, bonus points!')





class Shot(Drink):
    def __init__(self, drink_name, drink_type, *args: str, **kwargs: str) -> None:
        super().__init__(drink_name, drink_type, *args, **kwargs)

    def shake(self):
        print("You can't shake a shot!!! Booze has gone everywhere! Minus points")

    def add_ice(self):
        print("Customer has choked on your ice cube, minus points")

    




'''
class Order:
    def __init__(self, order_size) -> None:
        self.drinks_list = []
        self.menu_length = len(menu)
        self.order_size = order_size
        # print('menu length:', self.menu_length)

        for i in range(self.order_size):
            n = random.randint(0, self.menu_length - 1) 
            new_drink = Drink(menu[n])
            self.drinks_list.append(new_drink)


my_order = Order(4)
for drink in my_order.drinks_list:
    drink.guess_ingredients()
'''