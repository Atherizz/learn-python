import os
import json
# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status, priorities = line.strip(). split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status, "priorities" : priorities}
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} | {task['priorities']}  \n")
            
#add a new task
def add_task(tasks):
    title = input("enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title" : title, "status" : "incomplete", "priorities" : "No"}
    print(f"task {title} added.")
    
# view all tasks
def view_task(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        for task_id, task in tasks.items():
            print(f"{task_id} . {task['title']} | {task['status']} | priorities : {task['priorities']}")
            
# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("enter the task ID : "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"task {tasks[task_id]["title"]} mark as complete" )
    else:
        print("task ID not found, please input valid task ID!")
        
def set_task_priorities(tasks):
    task_id = int(input("enter the task ID : "))
    if task_id in tasks:
        tasks[task_id]["priorities"] = "yes"
        print(f"task {tasks[task_id]["title"]} set priorities" )
    else:
        print("task ID not found, please input valid task ID!")
        
def delete_task(tasks):
    task_id = int(input("enter the task ID : "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task {deleted_task['title']} was deleted" )
    else:
        print("task ID not found, please input valid task ID!")

def convert_json(tasks):
    save_tasks(tasks)
    tasks = load_tasks()
    
    formatted_json = {}
    for task_id, task in tasks.items():
        formatted_json[str(task_id)] = {
            "title": task["title"],
            "status": task["status"],
            "priorities": task["priorities"]
        }
    # if os.path.exists("output.json"):
    #     os.remove("output.json")

    with open("output.json", "w") as json_file:
        json.dump(formatted_json, json_file, indent=4, ensure_ascii=False)

        
# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Tasks")
        print("5. Set Priorities")
        print("6. Convert to JSON")
        print("7. Exit")
        choice = input("Enter your choice : ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            set_task_priorities(tasks)
        elif choice == "6":
            convert_json(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("Thanks!")
            break
        else:
            print("Invalid Choice, Please try again")
            
if __name__ == "__main__":
    main()
        