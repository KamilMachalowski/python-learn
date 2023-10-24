todos = []

#comment
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
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
