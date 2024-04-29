def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "The contact has been added successfully."
    except ValueError:
        return ("Make sure you follow the 'add username phone' template to add a contact.\n"
                "For example, 'add Bob 0123456789'")


def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "The contact has been changed successfully."
        else:
            return f"{name} in not in the contacts. Please use 'add' to add a new contact."
    except ValueError:
        return ("Make sure you follow the 'change phone username' template to change a contact's phone.\n"
                "For example, 'change Bob 0123456789'")


def display_contact(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            phone = contacts.get(name)
            return f"Name {name}. Phone {phone}."
        else:
            return f"{name} was not found."
    except IndexError:
        return ("Make sure you follow the 'phone username' template to display a contact's info.\n"
                "For example, 'phone Bob'")


def display_all_contacts(contacts):
    contacts_list = ""
    for key in contacts.keys():
        if key:
            contacts_list += f"Name: {key}. Phone: {contacts[key]}\n"
        else:
            break
    return contacts_list


def main():
    contacts = {}
    instruction = ("Please use the instruction below:\n"
                   "'add \x1B[3mphone username\x1B[0m' to add a new contact. "
                   "E.g. 'add Bob 0123456789'\n"
                   "'change \x1B[3mphone username\x1B[0m' to update an existing contact (phone). "
                   "E.g. 'change Bob 0987654321'\n"
                   "'phone \x1B[3musername\x1B[0m' to display a contact's info. E.g. 'phone Bob'\n"
                   "'all' to display all contacts\n")
    print("Welcome to the assistant manager! My name is Alex.")
    user_name = input("What's your name?\n").capitalize()
    print(f"Nice to meet you, {user_name}!\n\n{instruction}")

    while True:
        user_input = input("Please enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["exit", "close"]:
            print(f"Good bye, {user_name}!")
            break
        elif command in ["hello", "hi", "nice to meet you"]:
            print(f"How can I help you {user_name}?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(display_contact(args, contacts))
        elif command == "all":
            print(display_all_contacts(contacts))
        else:
            print("Sorry, I didn't quite catch you. Seems like you've provided an invalid command.\n"
                  f"{instruction}")


if __name__ == '__main__':
    main()
