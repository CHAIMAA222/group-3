import json, os
from datetime import datetime

FILE = "todos.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(data):
    json.dump(data, open(FILE, "w"), indent=2)

def add(data):
    t = input("Task: ")
    p = input("Priority (high/medium/low): ") or "medium"
    data.append({
        "id": len(data)+1,
        "title": t,
        "priority": p,
        "done": False,
        "time": str(datetime.now())[:16]
    })
    save(data)
    print("✔ added")

def show(data):
    print("\n--- TODO ---")
    for i in data:
        s = "✔" if i["done"] else "✗"
        print(f"{i['id']} [{s}] {i['title']} ({i['priority']})")

def done(data):
    show(data)
    try:
        x = int(input("ID: "))
        for i in data:
            if i["id"] == x:
                i["done"] = True
        save(data)
    except:
        print("error")

def delete(data):
    show(data)
    try:
        x = int(input("ID: "))
        data[:] = [i for i in data if i["id"] != x]
        save(data)
    except:
        print("error")

def menu():
    data = load()
    while True:
        print("\n1-add 2-show 3-done 4-delete 5-exit")
        c = input("> ")

        if c == "1":
            add(data)
        elif c == "2":
            show(data)
        elif c == "3":
            done(data)
        elif c == "4":
            delete(data)
        elif c == "5":
            break
        else:
            print("invalid")

menu()
