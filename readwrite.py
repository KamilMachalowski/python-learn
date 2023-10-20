while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("readwrite.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("readwrite.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("readwrite.txt", "r")
            todos = file.readlines()
            file.close()

            # todos_without_space = [item.strip("\n") for item in todos]

            # for index, item in enumerate(todos_without_space):
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")
        case "edit":
            number_of_todo = int(input("Number of todo to edit: ")) - 1
            todos[number_of_todo] = input("Enter new todo: ")
        case "complete":
            number_of_todo = int(input("Number of todo to complete: ")) - 1
            removed_element = todos.pop(number_of_todo)
            print(f"Todo {removed_element} completed!")
        case "exit":
            break

print("Bye Bye!")
