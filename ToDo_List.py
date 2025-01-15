exit = False
list_items = []


def cart_list(command):
    _, argument = command.split(" ", maxsplit = 1)
    return argument

def process_commands(command):
    exit = False
    
    if command.startswith("exit"):
        exit = True

    if command.startswith("add"):
        # adds items
        result = cart_list(command)
        print(f'Item in there carts: {result}')
        list_items.append(result)

    if command.startswith("delete"):
        # deletes items
        result = cart_list(command)
        print(f'Deleting item in cart: {result}')
        for item in list_items:
            if result == item:
                list_items.remove(item)
            else:
                print("Item not in list")
                break
    
        # display in list format
    for index, item in enumerate(list_items):
        print(f'{index + 1}. {item}')

    return exit

while not exit:
    command = input("Enter the command Add, Delete, or Exit: ").strip().lower() #removes any extra spaces and uppercase letters
    exit = process_commands(command)