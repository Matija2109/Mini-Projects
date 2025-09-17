tasks = []

def main():
    while True:
        print("----====+====----")
        print(" 1. Add task \n 2. Remove task \n 3. View tasks \n 4. Quit")
        try:
            choice = int(input("Choose your option:"))
        except ValueError:
            print("----====+====----")
            print("Invalid input, try again!")
            continue
        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            print("----====+====----")
            for i, task in enumerate(tasks, start = 1):
                print(i, task)
        elif choice == 4:
            print("----====+====----")
            print("Goodbye!")
            break
        else:
            print("----====+====----")
            print("Invalid input, try again!")

def add_task():
    print("What would you like to add:")
    task = input()
    tasks.append(task)

def remove_task():
    print("----====+====----")
    if len(tasks) != 0:
        for i, task in enumerate(tasks, start = 1):
            print(i, task)
        removal = int(input("Which task would you like to remove:"))
        tasks.pop(removal - 1)
        print("Task succesfully removed!")
    else:
        print("There are no tasks to remove!")


main()

