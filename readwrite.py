def get_todos(filepath="readwrite.txt"):
    """
    Read the text file and
    return the list of to-do items
    """
    with open(filepath, "r") as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(todos_arg, filepath="readwrite.txt"):
    """
    Write the to-do items list in the file.
    :param todos_arg: list with to-do
    :param filepath: filepath to file to read
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add [text], show, edit [number], complete [number] or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number_of_todo = int(user_action[5:]) - 1

            todos = get_todos()

            todos[number_of_todo] = input("Enter new todo: ") + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number_of_todo = int(user_action[8:]) - 1

            todos = get_todos()

            removed_element = todos.pop(number_of_todo).strip('\n')

            write_todos(todos)

            print(f"Successfully removed: {removed_element}")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not known")

print("Bye Bye!")
