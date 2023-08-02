import sys

contacts = {}

def input_error(input_data):
    def wrap(*args, **kwargs):    
        try:
            return input_data(*args, **kwargs)
        except (IndexError, ValueError, KeyError) as e:
            return "Give me name and phone please:"
    return wrap


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact '{name}' with phone '{phone}' added"

@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return f"Number'{phone}' for Contact '{name}' changed"

@input_error
def get_phone(name):
    return contacts[name]

def show_all():
    if len(contacts) == 0:
        return "No contacts found"
    else:
        result = ""
        for name, phone in contacts.items():
            result += "{}: {}\n".format(name, phone)
        return result

def handle_command(command):
    parts = command.split()
    if parts[0].lower() == "hello":
        return "Hello!"
    elif parts[0].lower() == "add":
        if len(parts) < 3:
            raise ValueError
        name = parts[1]
        phone = parts[2]
        return add_contact(name, phone)
    elif parts[0].lower() == "change":
        if len(parts) < 3:
            raise ValueError
        name = parts[1]
        phone = parts[2]
        return change_contact(name, phone)
    elif parts[0].lower() == "phone":
        if len(parts) < 2:
            raise ValueError
        name = parts[1]
        return get_phone(name)
    elif parts[0].lower() == "show" and parts[1].lower() == "all":
        return show_all()
    elif parts[0].lower() in ["good", "bye", "close", "exit"]:
        print("Good bye!")
        sys.exit()
    else:
        raise ValueError

def main():
    while True:
        command = input("Enter user name and phone please:")
        try:
            response = handle_command(command)
            print(response)
        except  (IndexError, ValueError, KeyError) as e:            
            print("Wrong input. Please try again:")

if __name__ == "__main__":
    main()