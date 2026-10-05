# Team Tasks

A deliberately small Python command-line task manager for learning Git and
GitHub collaboration. Add tasks, list them, mark them complete, search titles,
and view statistics. Each computer stores its own task data in JSON.

**Workshop starter:** this version contains three intentional bugs. Passing
starter tests do not imply every edge case works. See `docs/ISSUES.md`.

## Requirements

Python 3.10 or newer and Git. No pip installation, database, account credentials,
or third-party Python libraries are needed to run the app. GitHub collaboration
and hosted CI require internet access; the app and local tests work offline.
Commands use `python`; use `python3` or `py` if that is your Python launcher.

## Run

From the extracted project folder (the folder containing this README):

```sh
python -m team_tasks add "Prepare the workshop"
python -m team_tasks add "Review a pull request"
python -m team_tasks list
python -m team_tasks done 1
python -m team_tasks search "Review"
python -m team_tasks stats
python -m unittest discover -s tests -v
```

Custom storage: `python -m team_tasks --file data/demo.json list`.
Put `--file` before the subcommand. Default storage is relative to your current
directory. Personal data under `data/` is ignored by Git.

## Code map

- `team_tasks/tasks.py`: business logic; easiest place to start.
- `team_tasks/storage.py`: JSON loading and saving.
- `team_tasks/cli.py`: argument parsing and terminal output.
- `tests/`: 10 starter tests using Python's built-in unittest.
- `.github/`: CI workflow and issue/PR templates.
- `docs/ISSUES.md`: 14 contribution tasks with acceptance criteria.
- `docs/WORKSHOP.md`: instructor setup and a 90-minute lesson.
- `CONTRIBUTING.md`: contributor workflow and review expectations.

Task shape: `{"id": 1, "title": "Learn Git", "done": false}` in JSON.
IDs are integers, titles are strings, and done is a boolean. New IDs use the
largest currently stored ID plus one. This is a local, single-user teaching
app; simultaneous writes and hostile/malformed task files are out of scope.

## Workshop description

A small task manager built together, one pull request at a time.
