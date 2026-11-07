


def add_a_task():
    enter_task = input("Enter your task: ")
    new_task = {
    "name": enter_task,
    "completed": False
}
    tasks.append(new_task)
    
def view_tasks():
    if not tasks:
        print("No tasks yet")
        return
    else:
        print ("Tasks")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task['name']}")

def mark_task_as_completed():
    if not tasks:
            print ("No tasks yet")
            return
            
    try:
        task_com = int(input("Enter task no: "))
        if not 1 <= task_com <= len(tasks):
            print("No task with this no")
            return
        index = task_com - 1
        tasks[index]["completed"] = True
        print (f"Task no {task_com} marked completed")
    except ValueError:
        print ("Invalid Entry")
    


def delete_a_task():
    if not tasks:
            print ("No tasks yet")
            return
            
    try:
        dele = int(input("Enter task no: "))
        if not 1 <= dele <= len(tasks):
            print("No task with this no")
            return
        index = dele - 1
        tasks.pop(index)
        print (f"Task no {dele} deleted")
    except ValueError:
        print ("Invalid Entry")
        
    


actions = {
                    "1": add_a_task,
                    "2": view_tasks,
                    "3": mark_task_as_completed,
                    "4": delete_a_task,
}


tasks = []
#for task in tasks:
    #print(task)
#for number, task in enumerate(tasks, start=1):
    #print(number, task)

while True:
    
    print ("MENU")
    print ("1. Add a task")
    print ("2. View tasks")
    print ("3. Mark task as completed")
    print ("4. Delete a task")
    print ("5. Exit")


    choice = input("Choose an option: ")

    if choice in actions:
        actions[choice]()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice") 
    

    
