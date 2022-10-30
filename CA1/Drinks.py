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
    drink_name: ClassVar[str]
    __ingredients: ClassVar[list] # hidden from the user

    def __init__(self, drink_name, *args:str, **kwargs:str) -> None:
        self.drink_name = drink_name
        self.__ingredients = []
        self.complete = False
        self.current_rating = 0


    def __str__(self):
        output = self.drink_name
        return output

    def hint(self):
        hint = self.__ingredients[0]
        front_jumbled = 'b' + hint[1:]
        end_jumbled = hint[:-1] + 'y'
        print(f'You ask the drunken customer what they think is in a {self.drink_name}' \
            + f'"Well I reckon there might be some uhhhh, {front_jumbled}? {end_jumbled}???"')



    def add(self, ingredient):
        if ingredient in self.__ingredients:
            self.__ingredients.remove(ingredient)
            print(f"Good choice, {ingredient} has now been added")
        else:
            print(f"The customer tells you that there's no {ingredient} in a {self.drink_name}. You quickly knock back the {ingredient} to hide your shame.")

    def add_whipped_cream(self):
        successful = bool(random.randint(0, 1))
        if successful:
            print("Odd choice, but the customer loves it! Bonus points!")
            self.current_rating += 1
        else:
            print("The customer is lactose intolerant and afraid. Minus points.")
            self.current_rating -= 1

    def serve(self):
        missing = len(self.__ingredients)
        if missing > 0:
            print(f"Are you sure you want to continue? {missing} ingredients are still missing.")
            serving_decision = input('a: Keep preparing the drink \tb: Serve it as is \tc: Cry\n')
            if serving_decision == 'a':
                print("That's the spirit!")
            elif serving_decision == 'b':
                self.current_rating -= missing * 3
                self.complete = True
            elif serving_decision == 'c':
                print("Your tears add flavour to the drink, bonus points.")
        




class Cocktail(Drink):
    def __init__(self, drink_name, *args: str, **kwargs: str) -> None:
        super().__init__(drink_name, *args, **kwargs)
        self.__ingredients = cocktails_recipes[self.drink_name] 

    def shake(self):
        print('The customer was impressed by your shaking skills, bonus points!')
        self.current_rating += 1

    def add_ice(self):
        print('Ice added successfully, bonus points!')
        self.current_rating += 1





class Shot(Drink):
    def __init__(self, drink_name, *args: str, **kwargs: str) -> None:
        super().__init__(drink_name, *args, **kwargs)
        self.__ingredients = shots_recipes[self.drink_name]

    def shake(self):
        print("You can't shake a shot!!! Booze has gone everywhere! Minus points")
        self.current_rating -= 1

    def add_ice(self):
        print("Customer has choked on your ice cube, minus points")
        self.current_rating -= 1

    


class Order:
    total_score = 0
    

    def __init__(self, order_size = 5) -> None:
        self.drinks_list = []
        self.menu_length = len(menu)
        self.order_size = order_size
        self.current_score = 0

        for i in range(self.order_size):
            n = random.randint(0, self.menu_length - 1) 
            new_drink = menu[n]
            if new_drink in cocktails_recipes:
                self.drinks_list.append(Cocktail(new_drink))
            elif new_drink in shots_recipes:
                self.drinks_list.append(Shot(new_drink))

    def prepare_order(self):
        for drink in self.drinks_list:

            while not drink.complete:

                try:
                    exec(input('>>> '))
                except:
                    print("That input is not recognised")

            score = drink.current_rating

            self.total_score += score

            if score < 0:
                print('The customer is not happy with your drink, but knocks it back like a true soldier')
            elif score == 0:
                print('The customer is satisfied with your drink')
            else:
                print('The customer loves your drink and is emailing their mother about it already')



            


my_order = Order(4)
# my_order.prepare_order()
shot = Shot('scooby snack')
shot.hint()

