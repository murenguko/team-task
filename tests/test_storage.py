import tempfile
import unittest
from pathlib import Path
from team_tasks.storage import load_tasks, save_tasks

class StorageTests(unittest.TestCase):
    def test_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_tasks(Path(folder) / "absent.json"), [])

    def test_round_trip_and_nested_directory(self):
        tasks = [{"id": 1, "title": "Préparer l’atelier", "done": False}]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "tasks.json"
            save_tasks(path, tasks)
            self.assertEqual(load_tasks(path), tasks)

    def test_save_replaces_previous_contents(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            save_tasks(path, [{"id": 1, "title": "Old", "done": True}])
            save_tasks(path, [])
            self.assertEqual(load_tasks(path), [])
