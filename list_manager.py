# This is the list that will be operated on by all the other functions
my_list = []

def get_list():
    return(my_list)

def reset_list():
    my_list.clear()

def add_to_list(item):
    my_list.append(item)

def remove_from_list(item):
    if item not in my_list:
        raise ValueError
    my_list.remove(item)

def replace_item_in_list(item, replacement):
    if item not in my_list:
        raise ValueError
    index = my_list.index(item)
    my_list[index] = replacement

def get_item_at_position(position):
    if position < 1 or position > len(my_list):
        raise ValueError
    return my_list[position - 1]
