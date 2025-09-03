import datetime as dt
from random import randint
import json
import os

# read a .json file and return it
def read_file(path: str) -> list:
    with open(path, "r") as file:
        json_file = json.load(file)
        file.close()
    
    return json_file


# write a .json file
def write_file(path: str, json_files: list) -> None:
    with open(path, "w") as file:
        file.writelines(json.dumps(json_files, indent=4))
        file.close()

# show Commands
def show_help():
    print("Task-CLI manager\n")
    print("Commands:\n")
    print("help -> show commands\n")
    print("add [task] -> add a new task")
    print("update [id] [task] -> change task description")
    print("delete [id] [task] -> delete a task\n")
    print("list -> list all tasks\n")
    print("list-to-do -> list all tasks with state to-do")
    print("list-in-process -> list all tasks with state in-process")
    print("list-done -> list all tasks with state done\n")
    print("mark-to-do [id] -> mark task as to-do")
    print("mark-done [id] -> mark task as done")
    print("mark-in-process [id] -> mark task as in-process\n")
    print("use example -> task-cli add \"example task\"")

# generate unique string ids for every task
def id_generator() -> str:
    letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

    id = ""
    while len(id) < 5:
        id += letters[randint(0,len(letters)-1)]

    return id

def create_new_task(path: str, task: dict) -> str:
    if os.path.exists(path):
        json_file = read_file(path)
        json_file.append(task)
        write_file(path,json_file)

        return task["id"]
    else:
        json_file = []
        json_file.append(task)

        write_file(path, json_file)

        return task["id"]

def lists_task(path: str, status = None) -> None:
    if os.path.exists(path):
        if status == None:
            json_file = read_file(path)
            for i in json_file:
                print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")
        
        elif status == "to-do":
            json_file = read_file(path)

            for i in json_file:
                if i["status"] == status:
                    print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")

        elif status == "in-process":
            json_file = read_file(path)

            for i in json_file:
                if i["status"] == status:
                    print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")

        elif status == "done":
            json_file = read_file(path)

            for i in json_file:
                if i["status"] == status:
                    print(f"task id: {i["id"]}\ntask description: {i["desc"]}\ntask status: {i["status"]}\ntask creation date: {i["createdAt"]}\ntask update date: {i["updatedAt"]}\n")

def mark_tasks(path: str, id: str, status: str) -> None:
    if os.path.exists(path):
        if status == "to-do":
            json_file = read_file(path)

            for i in json_file:
                if i["id"] == id:
                    i.update({
                        "status":status,
                        "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                        })
                    write_file(path, json_file)
                    print("Task marked successfully!")
                    break
            else:
                print("Task id not found")

        elif status == "in-process":
            json_file = read_file(path)

            for i in json_file:
                if i["id"] == id:
                    i.update({
                        "status":status,
                        "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                        })
                    write_file(path, json_file)
                    print("Task marked successfully!")
                    break
            else:
                print("Task id not found")

        elif status == "done":
            json_file = read_file(path)

            for i in json_file:
                if i["id"] == id:
                    i.update({
                        "status":status,
                        "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                        })
                    write_file(path, json_file)
                    print("Task marked successfully!")
                    break
            else:
                print("Task id not found")

def delete_task(path: str, id: str) -> bool:
    json_file = read_file(path)

    for i in json_file:
        if i["id"] == id:
            json_file.pop(json_file.index(i))
            write_file(path, json_file)
            return True
    else:
        return False

def update_task(path: str, id: str, task: str) -> bool:
    json_file = read_file(path)

    for i in json_file:
        if i["id"] == id:
            i.update({
                "desc":task,
                "updatedAt":str(dt.datetime.now(dt.timezone.utc))
                })
            write_file(path, json_file)
            return True

    else:
        return False
