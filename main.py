import json
file = open("tasks.json", "w")
choice = input("Enter option: ")
"""
while choice != "1":
    if choice == "2":
        """
task = input("Enter task: ")
id = 1
x = {"id" : id, "task" : task }
y = json.dumps(x)
print(y)

file.write(y)

