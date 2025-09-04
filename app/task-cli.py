import sys
from services import create_new_task, id_generator, show_help, update_task
import os
import datetime as dt
import json

path = "data.json"

json_file = []
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        task = str(sys.argv[2])
        file = {
            "id":id_generator(),
            "desc":task,
            "status":"to-do",
            "createdAt":str(dt.datetime.now(dt.timezone.utc)),
            "updatedAt":str(dt.datetime.now(dt.timezone.utc))
            }

        result = create_new_task(path, file)
        print(f"Task added successfully with id: {result}")

    elif command == "update" and len(sys.argv) > 3:
        if os.path.exists(path):
            id = str(sys.argv[2])
            task = sys.argv[3]
            
            result = update_task(path, id, task)
            if result == True:
                print("Task updated")
            else:
                print("Task id not found")

        else:
            print("There's no file to update")
    
    elif command == "list":
        with open(path, 'r') as file:
            json_file = json.load(file)
            for i in json_file:
                print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")
            file.close()

    elif command == "delete" and len(sys.argv) > 2:
        id = str(sys.argv[2])

        with open(path, "r") as file:
            json_file = json.load(file)
            file.close()

        for i in json_file:
            if i["id"] == id:
                json_file.pop(json_file.index(i))
                with open(path, "w") as file:
                    file.writelines(json.dumps(json_file, indent=4))
                    file.close()
                print("Task Deleted")
                break
        else:
            print("Task id not found")

    elif command == "mark-done" and len(sys.argv) > 2:
        id = str(sys.argv[2])

        with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

        for i in json_file:
            if i["id"] == id:
                i.update({
                    "status":"done",  
                    "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                    })
                with open(path, "w") as file:
                    file.writelines(json.dumps(json_file, indent=4))
                    file.close()
                print("Task marked successfully!")
                break
        else:
            print("Task id not found")

    elif command == "mark-in-process" and len(sys.argv) > 2:
        id = str(sys.argv[2])

        with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

        for i in json_file:
            if i["id"] == id:
                i.update({
                    "status":"in-process",
                    "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                    })
                with open(path, "w") as file:
                    file.writelines(json.dumps(json_file, indent=4))
                    file.close()
                print("Task marked successfully!")
                break
        else:
            print("Task id not found")

    elif command == "list-to-do" and len(sys.argv) > 1:
        to_do_tasks = []

        with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

        for i in json_file:
            if i["status"] == "to-do":
                to_do_tasks.append(i)
        
        for i in to_do_tasks:
                print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")

    elif command == "list-in-process" and len(sys.argv) > 1:
        to_do_tasks = []

        with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

        for i in json_file:
            if i["status"] == "in-process":
                to_do_tasks.append(i)
        
        for i in to_do_tasks:
                print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")

    elif command == "list-done" and len(sys.argv) > 1:
        to_do_tasks = []

        with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

        for i in json_file:
            if i["status"] == "done":
                to_do_tasks.append(i)
        
        for i in to_do_tasks:
                print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")

    elif command == "help":
        show_help()

else:
    print("not enough arguments to execute this command")
