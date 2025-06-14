tasks = []

def add_task(text):
    tasks.append({"text": text, "done": False})

def get_tasks():
    return tasks

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
