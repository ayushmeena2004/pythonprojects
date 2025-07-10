#list
#add task
#update task
#delete task
todo = ["gym"]

while True:
    print("---Today's Task---")
    choice = int(input("1 for add task\n2 for update\n3 for delete\n4 for exit\nChoose your operation> "))

    if choice == 1:
        task = input("Enter the task: ")
        todo.append(task)
        print(f"Your today's tasks are: {todo}")

    elif choice == 2:
        yourtask = input("Enter a task to update: ")
        if yourtask in todo:
            ind = todo.index(yourtask)
            newtsk = input("Enter the new task: ")
            todo[ind] = newtsk
            print(f"Your today's tasks are: {todo}")
        else:
            print(f"{yourtask} is not in your todo list")

    elif choice == 3:
        yourtask = input("Enter a task to delete: ")
        if yourtask in todo:
            todo.remove(yourtask)
            print(f"Your today's tasks are: {todo}")
        else:
            print(f"{yourtask} is not in your todo list")

    elif choice == 4:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")


    


