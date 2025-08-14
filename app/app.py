import sys
import os
import datetime as dt
import json

path = os.path.join("tasks", "data.json")

json_file = []
index = len(json_file) + 1
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        task = str(sys.argv[2])
        if os.path.exists(path):
            with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

            json_file.append({
                "id":len(json_file)+1,
                "desc":task,
                "status":"to-do",
                "createdAt":str(dt.datetime.now(dt.timezone.utc)),
                "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                })

            with open(path, "w") as file:
                file.writelines(json.dumps(json_file, indent=4))
                file.close()

            print("Task added successfully!")
        else:
            json_file.append({
                "id":index,
                "desc":task,
                "status":"to-do",
                "createdAt":str(dt.datetime.now(dt.timezone.utc)),
                "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                })
        
            with open(path, "w") as file:
                file.writelines(json.dumps(json_file, indent=4))
                file.close()

            print("Task added successfully!")

else:
    run = True
    print("Task Manager Initialized\n")

    while run:
        print("Choose an option from below:")
        print("1. Create new file\n2. Access to a file\n3. Exit")
        option = input("Select one option: ")

        if option == "1":
            name = input("name: ")
        
            task = input("\nWrite a task to be added: ")
            json_file.append({
                    "id":index,
                    "desc":task,
                    "status":"to-do",
                    "createdAt":f"{dt.datetime.now(dt.timezone.utc)}",
                    "updatedAt":f"{dt.datetime.now(dt.timezone.utc)}"
                    })

            with open(f"tasks/{name}.json", "w") as file:
                file.writelines(json.dumps(json_file, indent=4))
                print("Task added successfully!\n")
                file.close()

            while run:
                print("Choose what to do now:\n1. Add new task\n2. Update existing task\n3. Delete a task\n4. List all tasks\n5. Exit")
                option = input("Select an option or write exit to quit: ")

                if option == "1":
                    task = input("\nWrite a task to be added: ")

                    json_file.append({
                        "id":index,
                        "desc":task,
                        "status":"to-do",
                        "createdAt":f"{dt.datetime.now(dt.timezone.utc)}",
                        "updatedAt":f"{dt.datetime.now(dt.timezone.utc)}"
                        })

                    with open(f"tasks/{name}.json", "w") as file:
                        file.writelines(json.dumps(json_file,  indent=4))
                        file.close()
            
                elif option == "2":
                    task_id = int(input("\nWrite the id of the task you want to update: "))
                
                    print(json_file[task_id-1]["desc"])


