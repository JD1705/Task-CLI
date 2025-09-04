import sys
from services import create_new_task, delete_task, id_generator, lists_task, mark_tasks, show_help, update_task
import os
import datetime as dt

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
        lists_task(path)

    elif command == "delete" and len(sys.argv) > 2:
        id = str(sys.argv[2])
        result = delete_task(path, id)

        if result == True:
            print("Task deleted")
        else:
            print("Task id not found")
    
    elif command == "mark-to-do" and len(sys.argv) > 2:
        id = str(sys.argv[2])
        state = "to-do"
        mark_tasks(path, id, state)

    elif command == "mark-done" and len(sys.argv) > 2:
        id = str(sys.argv[2])
        state = "done"
        mark_tasks(path, id, state)

    elif command == "mark-in-process" and len(sys.argv) > 2:
        id = str(sys.argv[2])
        state = "in-process"
        mark_tasks(path, id, state)

    elif command == "list-to-do" and len(sys.argv) > 1:
        state = "to-do"
        lists_task(path, state)

    elif command == "list-in-process" and len(sys.argv) > 1:
        state = "in-process"
        lists_task(path, state)

    elif command == "list-done" and len(sys.argv) > 1:
        state = "done"
        lists_task(path, state)

    elif command == "help":
        show_help()

else:
    print("not enough arguments to execute this command")
