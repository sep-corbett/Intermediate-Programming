# ddfine a function with dunder

def a_function(a_param: int) -> str:
    '''
    list types of params etc
    -> gives hints in vscode
    '''
    return a_param



if __name__ == "__main__":
    # only if this is the file being called
    # print(a_function.__doc__) # prints docstream comment
    pass 


# nested loops

my_list = []

for val in range(5):
    for val2 in range(6, 9):
        # print(val, "+", val2, "=", val+val2)
        my_list.append(val+val2)

# dictionaries

my_dict = {}
my_list = []
my_set = ()

# keys, values

for index, val in enumerate(range(4, 9)):
    my_dict[index] = val

print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for key, val in my_dict.items():
    print(key, val)


# recursion

def recursion_func(a_value: int) -> str:
    '''
    count down and blast off, from a given number
    '''

    if a_value <= 0:
        return ("Blast off!")
    else:
        return f"{a_value}\n" + recursion_func(a_value - 1)

    # for val in range(a_value, 0, -1):
    #     print(val)
    # print("Blast off!")

    pass

recursion_func(5)

print('\n')


i = -1

while i < 20:
    i += 1 
    if i % 2 == 0:
        print(i, "even")
        if i == 14:
            break

    else:
        if i == 11:
            continue
        print(i, "odd")
        pass
    
    