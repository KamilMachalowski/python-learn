while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("readwrite.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("readwrite.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("readwrite.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")
        case "edit":
            number_of_todo = int(input("Number of todo to edit: ")) - 1

            with open("readwrite.txt", "r") as file:
                todos = file.readlines()

            todos[number_of_todo] = input("Enter new todo: ") + "\n"

            with open("readwrite.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            number_of_todo = int(input("Number of todo to complete: ")) - 1

            with open("readwrite.txt", "r") as file:
                todos = file.readlines()

            removed_element = todos.pop(number_of_todo).strip('\n')

            with open("readwrite.txt", "w") as file:
                file.writelines(todos)

            print(f"Successfully removed: {removed_element}")
        case "exit":
            break

print("Bye Bye!")
