# create dictionary of drinks from text file
drinks_dict = {}
drinks_list = []

with open('Cocktails.txt', 'r') as file:
    for line in file:
        line = line.strip()
        drink, ingredients = line.split(': ')
        ingredients = ingredients.split(', ')
        # print(drink, ingredients)
        drinks_dict[drink] = ingredients
        drinks_list.append(drink)

# create dictionary of ingredients by type
ingredients_dict = {}

with open('Ingredients.txt', 'r') as file:
    for line in file:
        line = line.strip()
        type, ingredients = line.split(': ')
        ingredients = ingredients.split(', ')
        ingredients_dict[type] = ingredients

# print('drinks dict')
# for item in drinks_dict:
#     print(item, drinks_dict[item])
# print('\ningredients dict')
# for item in ingredients_dict:
#     print(item, ingredients_dict[item])

class Drink:
    def __init__(self, drink_name) -> None:
        try:
            self.name = drinks_list[int(drink_name)]
        except:
            self.name = drink_name.lower()

        self.ingredients = drinks_dict[self.name]
        # print(self.name, self.ingredients)
        self.spirits = []
        self.mixers = []
        self.syrups = []
        self.garnishes = []

        self.categorise_ingredients()
        # if args is just number, select random drink

        # print((drink_name))

    def categorise_ingredients(self):
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

    def list_ingredients(self):
        print(self.name)
        print('spirits: ', [item for item in self.spirits])
        print('mixers: ', [item for item in self.mixers])
        print('syrups: ', [item for item in self.syrups])
        print('garnishes: ', [item for item in self.garnishes])


class Order:
    def __init__(self) -> None:
        self.drinks_list = []
        
        for i in range(5):
            n = i # change to random number
            # input random number in correct range
            new_drink = Drink(drinks_list[n])

mydrink = Drink(1)
mydrink.list_ingredients()