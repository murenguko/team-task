"""Local JSON persistence; missing files represent an empty task list."""
import json
from pathlib import Path

def load_tasks(path):
    path = Path(path)
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as source:
        return json.load(source)

def save_tasks(path, tasks):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as target:
        json.dump(tasks, target, indent=2, ensure_ascii=False)
        target.write("\n")
