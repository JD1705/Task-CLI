import sys
import os
import datetime as dt
import json
from random import randint

def id_generator() -> str:
    letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

    id = ""
    while len(id) < 5:
        id += letters[randint(0,len(letters)-1)]

    return id

path = "data.json"

json_file = []
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        task = str(sys.argv[2])
        if os.path.exists(path):
            with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

            json_file.append({
                "id":id_generator(),
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
                "id":id_generator(),
                "desc":task,
                "status":"to-do",
                "createdAt":str(dt.datetime.now(dt.timezone.utc)),
                "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                })
        
            with open(path, "w") as file:
                file.writelines(json.dumps(json_file, indent=4))
                file.close()

            print("Task added successfully!")
    elif command == "update" and len(sys.argv) > 3:
        if os.path.exists(path):
            id = str(sys.argv[2])
            task = sys.argv[3]

            with open(path, "r") as file:
                json_file = json.load(file)
                file.close()

            for i in json_file:
                if i["id"] == id:
                    i.update({
                        "desc":task,
                        "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                        })
                    with open(path, "w") as file:
                        file.writelines(json.dumps(json_file, indent=4))
                        file.close()
                    print("Task updated successfully!")
                    break
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
                    })
                with open(path, "w") as file:
                    file.writelines(json.dumps(json_file, indent=4))
                    file.close()
                print("Task marked successfully!")
                break
        else:
            print("Task id not found")

else:
    print("not enough arguments to execute this command")
