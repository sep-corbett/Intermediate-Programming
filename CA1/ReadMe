# Welcome to the bar! 
## Here's some important information to read before your first shift!

Generating and preparing an order should be done as follows, with n being the number of drinks in the order:

```
my_order = Order(n)
my_order.prepare()
``` 

From there, you will be given the name of your first drink, and a terminal will appear.
Into this terminal, you can write python code that will be executed.

To add an ingredient to a drink (for example vodka):
`>>> drink.add('vodka')`

Here are some additional operations you can you to potentially increase/decrease the quality of your drink:
```
>>> drink.add_ice()
>>> drink.shake()
>>> drink.add_whipped_cream()
```

When you feel the drink is ready, run:
`>>> drink.serve()`

There will be penalties for missing ingredients. 
You can ask the customer for a hint by entering any input with the word 'hint' in it.
`>>> please give me a hint pretty please`


## Code analysis
# Encapsulation
Used to hide some of the private details of a class from other objects.
For example, the __generate_order() function can only be called within the Order class.
(see lines 165 and 170)

# Inheritance
The Cocktail and Shot classes are subclasses/child classes of the Drink parent class.
They inherit several attributes and methods from the Drink class
(see lines 112 and 137)

# Polymorphism
The shake() and add_ice() methods run different code for Cocktails and Shots.
(see lines 117 and 142)


