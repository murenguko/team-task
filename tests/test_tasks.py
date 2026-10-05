import unittest
from team_tasks.tasks import add_task, complete_task, search_tasks, task_stats

class TaskTests(unittest.TestCase):
    def test_add_first_task(self):
        tasks = []
        self.assertEqual(add_task(tasks, "Learn Git"),
                         {"id": 1, "title": "Learn Git", "done": False})
        self.assertEqual(len(tasks), 1)

    def test_ids_follow_highest_existing_id(self):
        tasks = [{"id": 7, "title": "Existing", "done": False}]
        self.assertEqual(add_task(tasks, "New")["id"], 8)

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            add_task([], "")

    def test_complete_task(self):
        tasks = []
        add_task(tasks, "Review PR")
        self.assertTrue(complete_task(tasks, 1)["done"])

    def test_unknown_id_is_rejected(self):
        with self.assertRaises(ValueError):
            complete_task([], 99)

    def test_search_matching_text(self):
        tasks = []
        add_task(tasks, "Learn Git")
        add_task(tasks, "Write tests")
        self.assertEqual([t["id"] for t in search_tasks(tasks, "Git")], [1])

    def test_stats_for_nonempty_list(self):
        tasks = []
        add_task(tasks, "One")
        add_task(tasks, "Two")
        complete_task(tasks, 1)
        self.assertEqual(task_stats(tasks), {"total": 2, "completed": 1,
                         "pending": 1, "completion_percent": 50.0})
