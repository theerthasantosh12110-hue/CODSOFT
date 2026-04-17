t = []

while True:
    print("\nTo-Do List")
    print("1.Add task")
    print("2.View task")
    print("3.Update task")
    print("4.Delete task")
    print("5.Exit")

    u = int(input("Enter choice between 1 to 5: "))

    if u == 1:
        a = input("Enter task: ")
        t.append(a)
        print("Task added successfully!")

    elif u == 2:
        if len(t) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(t)):
                print(i + 1, ".", t[i])

    elif u == 3:
        b = int(input("Enter the task number to change: ")) - 1

        if 0 <= b < len(t):
            c = input("Enter new task: ")
            t[b] = c
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif u == 4:
        d = int(input("Enter the task number to delete: ")) - 1

        if 0 <= d < len(t):
            t.pop(d)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif u == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")

input("Press Enter to exit...")