from functions import get_todos,set_todos


mypath = "Todo.txt"
while True :
    user_action = input("Enter to(show ,add,edite,delete ,exit):")
    
    if user_action.startswith("show"):
        content = get_todos()
        
        for index , item in enumerate(content):
            item = item.strip('\n')
            row = "{}-{}".format(index+1,item)
            print(row)


    if user_action.startswith("add"):
        if len(user_action) == 3:
            new_todo = input("Enter new to do : ")
        else:
            new_todo = user_action[4:]

        with open(mypath , 'a') as file:
            content = file.writelines(new_todo+"\n")


    if user_action.startswith("delete"):
        try:
            if len(user_action) == 6:
                number_remove = int(input("Enter number to remove :"))
            else:
                number_remove = int(user_action[7:])

            content = get_todos()
            index = number_remove - 1
            to_do_removed = content[index]
            content.pop(index)
            
            set_todos(content)

            message = "{} was removed from the list".format(to_do_removed.strip("\n"))
            print(message)
        except IndexError:
            print("there is no item with that number.")


    if user_action.startswith("edite"):
        try:
            if len(user_action) == 5:
                number_edite = int(input("Enter number to edite :"))
            else:
                number_edite = int(user_action[5:])

            content = get_todos()
            index = number_edite - 1
            content[index] = input("enter the new value: ") +"\n"


            set_todos(content)

        except ValueError:
            print("your command is not valid.")

    if "exit" in user_action:
        break
    