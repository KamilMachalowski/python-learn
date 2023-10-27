FILE_PATH = "readwrite.txt"


def get_todos(filepath=FILE_PATH):
    """
    Read the text file and
    return the list of to-do items
    """
    with open(filepath, "r") as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(todos_arg, filepath=FILE_PATH):
    """
    Write the to-do items list in the file.
    :param todos_arg: list with to-do
    :param filepath: filepath to file to read
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
