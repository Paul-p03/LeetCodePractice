exit = False
list_items = []
filename = None

def cart_list(command):
    _, argument = command.split(" ", maxsplit = 1)
    return argument
    

def handle_add(command):
        # adds items
        result = cart_list(command)
        print(f'Item in there carts: {result}')
        list_items.append(result)
        print("current list: ")
        handle_list()


def handle_delete(command):
        # deletes items
        result = cart_list(command).lower().strip()
        print(f'Deleting item in cart: {result}')

        specific_item = False
        for item in list_items:
            if result == item.lower():
                list_items.remove(item)
                specific_item = True
                print(f'Item {item} deleted')
                break
        if not specific_item:
            print(f'Item {item} not found')
        print("Updated List: ")
        handle_list()

def handle_list():
    for index, item in enumerate(list_items):
        print(f'{index + 1}. {item}')

def open_file(command):
    global filename
    filename = get_filename(command)
    try:
        with open(filename, 'r') as file:
            if check_file(filename) == False:
                user_input = input("Type Y/N if you would like to clear the current list: ")
                if user_input.strip().lower() == "y":
                    print("Clearing existing list!")
                    list_items.clear(file)
             
            for line in file:        
                list_items.append(line.strip())
                print(f'file {filename} found')
    except:
        print(f'file {filename} not found')

def save_file(command):
    global filename
    filename = get_filename(command)
    with open(filename, 'w') as file:
        for list_item in list_items:
            file.write(f'{list_item}\n')
        print(f'{filename} saved successfully')

def get_filename(command):
    filename = cart_list(command)
    return filename + ".todo.txt"

def check_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip() == ""

def process_commands(command):
    global filename
    exit = False
    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        handle_add(command)
    elif command.startswith("delete"):
        handle_delete(command)
    elif command.startswith("list"):
        handle_list()
        # display in list format
    elif command.startswith("open"):
        open_file(command)
        print(f'Tasks loaded from file {filename}: ')
        handle_list()
    elif command.startswith("save"):
        save_file(command)
    else:
        print("Command Not Recognized")
    
    if exit and filename:
        save_file(command)
        print(f'Saved {filename} before exiting')

    return exit

while not exit:
    command = input("Enter the command Add, Delete, List, or Exit: ").strip().lower() #removes any extra spaces and uppercase letters
    exit = process_commands(command) 