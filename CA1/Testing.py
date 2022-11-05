# 121311053 Sarah Corbett
from Drinks import *

my_cocktail = Cocktail('white russian')
my_shot = Shot('baby guinness')


print('Cocktail is cocktail:', isinstance(my_cocktail, Cocktail))
print('Shot is drink:', isinstance(my_cocktail, Drink))
print('Shot is drink:', isinstance(my_shot, Drink))
print('Shot is shot:', isinstance(my_shot, Shot))
print('Shot is cocktail:', isinstance(my_shot, Cocktail), '\n')


# These two methods will run different code as they are different objects (polymorphism)
my_cocktail.shake()
my_shot.shake()


my_order = Order()
print('\nOrder list:', my_order.get_drinks_list())

# This will throw an error since the __generate_order() in private (enacpsulation)
# my_order.__generate_order()
my_order.prepare_order()
