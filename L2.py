# doesn't typecheck, just a suggestion/hint
from curses import A_UNDERLINE


def pass_in_a_number(a_number:int) -> int:
    return(str(a_number))


def strict_number(a_number:int) -> int:
    try:
        return type(str(a_number+1))
    except Exception as e:
        # return str(e) + f": {a_number}"
        return "not an int - " + str(e)

# def int_or_str(input: int|str) -> int:
#     return int(input) + 1


# 1, 0, 3
# 2, 1, 4
# 3, 2, 5
# 4, 3, 6
# 5, 4, 7

# a = [1, 2, 3, 4, 5]
# for i, j in enumerate(range(3, 8)):
#     print(a[i], i, j)
# ---


my_list =[]
for i in range(5):
    if i % 2 == 0:
        my_list.append(i*i)
    else:
        my_list.append(i)

# [0, 1, 4, 3, 16]
# print(my_list)

# print([i*i if i % 2 == 0 else i for i in range(5)])

# files - fine as either with or open/close

def read_file(filename:str) -> dict:
    my_dict = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip('\n').split()
                key, values_list = line[0], [int(i.strip()) for i in line[1:]]
                my_dict[key] = values_list
            
        for key in my_dict:
            print(key, my_dict[key])
        
    except:
        print("file not found")
        

read_file("temperatures.txt")

