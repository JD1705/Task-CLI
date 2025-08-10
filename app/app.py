import datetime as dt
import json

run = True
print("Task Manager Initialized")
while run:
    print("Choose an option from below:")
    print("1. Create new file\n2. Access to a file")
    option = int(input("Select one option: "))

    if option == 1:
        name = input("name: ")
        
        task = input("\nWrite a task to be added: ")
        id = 1
        json_file = {
                "id":id,
                "desc":task,
                "status":"to-do",
                "createdAt":f"{dt.datetime.now(dt.timezone.utc)}",
                "updatedAt":f"{dt.datetime.now(dt.timezone.utc)}"
                }
        with open(f"tasks/{name}.json", "w") as file:
            file.writelines(json.dumps(json_file, indent=4))
            file.close()
        run = False
