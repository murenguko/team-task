"""Task operations. Functions change the supplied list where appropriate."""

def add_task(tasks, title):
    if not title:
        raise ValueError("Title cannot be empty.")
    task = {"id": max((t["id"] for t in tasks), default=0) + 1,
            "title": title, "done": False}
    tasks.append(task)
    return task

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise ValueError(f"Task {task_id} not found.")

def search_tasks(tasks, query):
    return [task for task in tasks if query in task["title"]]

def task_stats(tasks):
    completed = sum(task["done"] for task in tasks)
    return {"total": len(tasks), "completed": completed,
            "pending": len(tasks) - completed,
            "completion_percent": round(completed / len(tasks) * 100, 1)}
