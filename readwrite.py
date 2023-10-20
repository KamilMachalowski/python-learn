while True:
    user_action = input("Type add [text], show, edit [number], complete [number] or exit: ").strip()

    if "add" in user_action:
        todo = user_action[4:] + "\n"

        with open("readwrite.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("readwrite.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("readwrite.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif "edit" in user_action:
        number_of_todo = int(user_action[5:]) - 1

        with open("readwrite.txt", "r") as file:
            todos = file.readlines()

        todos[number_of_todo] = input("Enter new todo: ") + "\n"

        with open("readwrite.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number_of_todo = int(user_action[8:]) - 1

        with open("readwrite.txt", "r") as file:
            todos = file.readlines()

        removed_element = todos.pop(number_of_todo).strip('\n')

        with open("readwrite.txt", "w") as file:
            file.writelines(todos)

        print(f"Successfully removed: {removed_element}")

    elif "exit" in user_action:
        break

    else:
        print("Command not known")

print("Bye Bye!")
