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

def list_tasks_done(path: str) -> list:
    done_list = []
    json_file = read_file(path)

    for i in json_file:
        if i["status"] == "done":
            done_list.append(i)

    return done_list

def list_tasks_todo(path: str) -> list:
    todo_list = []
    json_file = read_file(path)

    for i in json_file:
        if i["status"] == "to-do":
            todo_list.append(i)

    return todo_list

def list_tasks_inprocess(path: str) -> list:
    inprocess_list = []
    json_file = read_file(path)

    for i in json_file:
        if i["status"] == "in-process":
            inprocess_list.append(i)

    return inprocess_list

def lists_task(path: str) -> list:
    json_file = read_file(path)

    return json_file

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
