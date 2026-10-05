"""Command-line interface. Run from the repository root."""
import argparse
from .storage import load_tasks, save_tasks
from .tasks import add_task, complete_task, search_tasks, task_stats

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"{task['id']}. [{mark}] {task['title']}")

def main(argv=None):
    parser = argparse.ArgumentParser(description="Team Tasks: learn collaboration together.")
    parser.add_argument("--file", default="data/tasks.json", help="JSON storage path")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("add", help="Add a task").add_argument("title")
    commands.add_parser("list", help="List all tasks")
    commands.add_parser("done", help="Complete a task").add_argument("id", type=int)
    commands.add_parser("search", help="Search task titles").add_argument("query")
    commands.add_parser("stats", help="Show completion statistics")
    args = parser.parse_args(argv)
    try:
        tasks = load_tasks(args.file)
        if args.command == "add":
            task = add_task(tasks, args.title)
            save_tasks(args.file, tasks)
            print(f"Added task {task['id']}.")
        elif args.command == "done":
            complete_task(tasks, args.id)
            save_tasks(args.file, tasks)
            print(f"Completed task {args.id}.")
        elif args.command == "list":
            show_tasks(tasks)
        elif args.command == "search":
            show_tasks(search_tasks(tasks, args.query))
        elif args.command == "stats":
            for key, value in task_stats(tasks).items():
                print(f"{key}: {value}")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Error: {exc}\n")
