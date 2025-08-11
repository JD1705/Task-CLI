import os
import datetime as dt
import json

run = True
print("Task Manager Initialized")

while run:
    print("Choose an option from below:")
    print("1. Create new file\n2. Access to a file\n3. Exit")
    option = input("Select one option: ")

    if option == "1":
        name = input("name: ")
        
        task = input("\nWrite a task to be added: ")
        index = 1
        json_file = [{
                "id":index,
                "desc":task,
                "status":"to-do",
                "createdAt":f"{dt.datetime.now(dt.timezone.utc)}",
                "updatedAt":f"{dt.datetime.now(dt.timezone.utc)}"
                }]

        with open(f"tasks/{name}.json", "w") as file:
            file.writelines(json.dumps(json_file, indent=4))
            print("Task added successfully!\n")
            file.close()

        while run:
            print("Choose what to do now:\n1. Add new task\n2. Update existing task\n3. Delete a task\n4. Exit")
            option = input("Select an option or write exit to quit: ")

            if option == "1":
                task = input("\nWrite a task to be added: ")
                index = len(json_file) + 1

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
                

        run = False
