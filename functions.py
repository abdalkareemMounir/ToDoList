def get_todos(filepath="Todo.txt"):
    """read text file and return it's content"""
    with open(filepath, "r") as file_local:
            content_local = file_local.readlines()
    return content_local


def set_todos(new_to_do,filepath="Todo.txt"):
    """take file path and what to write"""
    with open(filepath , "w") as file:
                file.writelines(new_to_do)


if __name__ == "__main__":
    print("hello")