import json

def showMenu():
     print("\n------ Menu ------")
     print("1. View menu")
     print("2. View tasks")
     print("3. Add tasks")
     print("4. Complete task")
     print("5. Quit\n")

def addTasks():
     file = open("tasks.json", "a")
     tasks = {}
     id = 1
     status = "Incomplete"
     task = input("Enter task: ")
     while task:
          tasks[str(id)] = [task, status]
          id += 1
          task = input("Enter task: ")

     json.dump(tasks, file)
     file.close()

def showTasks():
     file = open("tasks.json", "r")
     try:
          tasks = json.load(file)
          for task in tasks:
               print(f"{task}. {tasks[task][0]}: {tasks[task][1]}")
          file.close()
     except:
          print("No tasks added.")

def completeTasks():
     file = open("tasks.json", "r+")
     tasks = json.load(file)
     id = input("Which task  do you want to mark as complete: ")
     tasks[id][1] = "Complete"
     print(f"{tasks[id][0]} marked as {tasks[id][1]}")
     file.close()
     file = open("tasks.json", "w")
     json.dump(tasks, file)
     file.close()

showMenu()

while True:
     choice = int(input("What do you want to do: "))
     print()
     if choice == 1:
          showMenu()
     elif choice == 2:
          showTasks()
     elif choice == 3:
          addTasks()
     elif choice == 4:
          completeTasks()
     elif choice == 5:
          break
     

print("\nProgram exited")