# 121311053 Sarah Corbett

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

class Drink:
    drink_name: ClassVar[str]
    _ingredients: ClassVar[list] # hidden from the user
    _shake_count: ClassVar[int]
    _cream_count: ClassVar[int]
    _hint_count: ClassVar[int]

    _cream_count = 5
    _shake_count = 3
    _hint_count = 3

    def __init__(self, drink_name, *args:str, **kwargs:str) -> None:
        self.drink_name = drink_name
        self._ingredients = args[0]
        
        self.complete = False
        self.current_rating = 0



    def __str__(self):
        output = self.drink_name
        return output

    def _hint(self):
        if Drink._hint_count <= 0:
            print('You cannot ask the customer any more questions as they are too sloshed.')
            return
        if len(self._ingredients) == 0:
            print('No hint needed, this drink is complete!')
            return 
        hint = self._ingredients[0]
        front_jumbled = 'b' + hint[1:]
        end_jumbled = hint[:-1] + 'y'
        print(f'You ask the drunken customer what they think is in a {self.drink_name}' \
            + f'\n"Well I reckon there might be some uhhhh, {front_jumbled}? {end_jumbled}???"')
        Drink._hint_count -= 1
        print(f'You have {Drink._hint_count} hints left.')



    def add(self, ingredient):
        if ingredient in self._ingredients:
            self._ingredients.remove(ingredient)
            print(f"Good choice, {ingredient} has now been added")
        else:
            print(f"The customer tells you that there's no {ingredient} in a {self.drink_name}. You quickly knock back the {ingredient} to hide your shame.")

    def add_whipped_cream(self):
        if Drink._cream_count <= 0:
            print('Oh no! You have run out of whipped cream!')
            return

        successful = bool(random.randint(0, 1))
        if successful:
            print("Odd choice, but the customer loves it! Bonus points!")
            self.current_rating += 1
        else:
            print("The customer is lactose intolerant and afraid. Minus points.")
            self.current_rating -= 1

        Drink._cream_count -= 1

    def serve(self):
        missing = len(self._ingredients)
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
        else:
            self.complete = True
            
        




class Cocktail(Drink):
    def __init__(self, drink_name, *args: str, **kwargs: str) -> None:
        ingredients_list = [item for item in cocktails_recipes[drink_name]]
        super().__init__(drink_name, ingredients_list)

    def __str__(self):
        return f"{self.drink_name} (cocktail)"

    def shake(self):
        if self._shake_count <= 0:
            print('Oh no! Your cocktail shaker has broken! Drink flies everywhere! The customers are damp. Minus points')
            self.current_rating -= 1
            return
        print('The customer was impressed by your shaking skills, bonus points!')
        self.current_rating += 1
        Drink._shake_count -= 1

    def add_ice(self):
        print('Ice added successfully, bonus points!')
        self.current_rating += 1





class Shot(Drink):
    def __init__(self, drink_name, *args: str, **kwargs: str) -> None:
        ingredients_list = [item for item in shots_recipes[drink_name]]
        super().__init__(drink_name, ingredients_list)

    def __str__(self):
        return f"{self.drink_name} (shot)"

    def shake(self):
        print("You can't shake a shot!!! Booze has gone everywhere! Minus points")
        self.current_rating -= 1

    def add_ice(self):
        print("Customer has choked on your ice cube, minus points")
        self.current_rating -= 1

    


class Order:
    total_score: ClassVar[int]
    menu: ClassVar[list]

    total_score = 0
    menu = list(cocktails_recipes.keys()) + list(shots_recipes.keys())

    def __init__(self, order_size = 5) -> None:
        self.__drinks_list = []
        self.order_size = order_size
        self.current_score = 0

        self.__generate_order()

    def get_drinks_list(self):
        return [str(drink) for drink in self.__drinks_list]

    def __generate_order(self):
        for i in range(self.order_size):
            n = random.randint(0, len(self.menu) - 1) 
            new_drink = self.menu[n]
            if new_drink in cocktails_recipes:
                self.__drinks_list.append(Cocktail(new_drink))
            elif new_drink in shots_recipes:
                self.__drinks_list.append(Shot(new_drink))

    def prepare_order(self):
        print('Welcome to your first shift at the bar! Make sure to read your instructions in the ReadMe')
        

        for drink in self.__drinks_list:
            print('Your order is:', drink.drink_name)
            while not drink.complete:
                a = input('>>> ')
                try:
                    exec(a)
                except:
                    if 'hint' in  a:
                        drink._hint()
                    else:
                        print("That input is not recognised")

            score = drink.current_rating

            self.total_score += score

            if score < 0:
                print('The customer is not happy with your drink, but knocks it back like a true soldier')
            elif score == 0:
                print('The customer is satisfied with your drink')
            else:
                print('The customer loves your drink and is emailing their mother about it already')

my_order = Order(1)
my_order.prepare_order()