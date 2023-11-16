import readwrite_modules
import time

now = time.strftime("%b %d, %Y %H %H:%M:%S")
print('now time ', now)

while True:
    user_action = input("Type add [text], show, edit [number], complete [number] or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = readwrite_modules.get_todos()

        todos.append(todo)

        readwrite_modules.write_todos(todos)

    elif user_action.startswith("show"):
        todos = readwrite_modules.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number_of_todo = int(user_action[5:]) - 1

            todos = readwrite_modules.get_todos()

            todos[number_of_todo] = input("Enter new todo: ") + "\n"

            readwrite_modules.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number_of_todo = int(user_action[8:]) - 1

            todos = readwrite_modules.get_todos()

            removed_element = todos.pop(number_of_todo).strip('\n')

            readwrite_modules.write_todos(todos)

            print(f"Successfully removed: {removed_element}")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not known")

print("Bye Bye!")
