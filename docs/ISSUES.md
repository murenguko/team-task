# Contribution backlog

Copy each selected task into a GitHub issue. Codes B1/F1/etc. are planning
identifiers, not GitHub issue numbers. All code changes must preserve existing
tests; features should include tests and updated usage examples.

## B1 — Fix statistics on an empty list (easy)
Reproduce: `python -m team_tasks --file data/empty.json stats` with no such file.
Actual: division-by-zero traceback. Expected: all four statistics are zero.
Acceptance: a regression test calls `task_stats([])` and checks the entire result.

## B2 — Reject whitespace-only titles (easy)
Reproduce: `python -m team_tasks add "   "`.
Actual: an apparently blank task is saved. Expected: ValueError for empty or
whitespace-only titles; strip surrounding whitespace from valid titles.
Acceptance: tests cover spaces, tabs, and `"  Learn Git  "`; invalid input must
not mutate the task list.

## B3 — Make search case-insensitive (easy)
Add `Learn Git`, then search `git`. Actual: no match. Expected: match.
Acceptance: mixed-case and no-match tests; preserve original title casing.
An empty query continues to return all tasks. Consider `str.casefold()`.

## F1 — Filter pending/completed tasks (easy–medium)
Add `list --status all|pending|done`, defaulting to all.
Acceptance: preserve insertion order; test empty and mixed task lists; argparse
rejects invalid status values. Implement filtering in a separate module.

## F2 — Delete a task (medium)
Add `delete ID`. Acceptance: remove only that ID, persist the result, raise a
useful error for unknown IDs, and cover both cases with tests. Remaining IDs
must not be renumbered. Do not promise global ID uniqueness after deletions.

## F3 — Rename a task (medium)
Add `rename ID "New title"`. Acceptance: preserve ID and completion state;
reject blank titles and unknown IDs; persist and test. Coordinate with B2
so title validation follows the same rules.

## F4 — Reopen a completed task (easy–medium)
Add `reopen ID`. Acceptance: done becomes false; reopening an already-pending
task is harmless; unknown IDs raise ValueError; include persistence and tests.

## F5 — Export CSV (medium)
Add `export OUTPUT_PATH` in a separate export module.
Acceptance: UTF-8 CSV with id/title/done header; quote commas/newlines correctly
using Python's csv module; empty lists produce a header; task data is unchanged.
Reject an output path resolving to the active JSON storage file to prevent
overwriting it. Tests use temporary directories.

## F6 — Sort displayed tasks (medium)
Add `list --sort id|title`, defaulting to id.
Acceptance: case-insensitive title order with ID as a tie-breaker; never change
stored order; test ties and empty input. Coordinate CLI integration with F1.

## T1 — Test CLI behavior (easy–medium)
Add tests using `cli.main([...])` plus temporary files and captured stdout/stderr.
Acceptance: add/list/done work together; missing ID yields exit code 1 and a
readable error; tests never touch `data/tasks.json` or depend on execution order.

## T2 — Expand business-logic coverage (easy)
Acceptance: completing an already-complete task is harmless, an unmatched
search returns [], and a search does not mutate its input. Keep independent
fixtures and descriptive test names. Coordinate with B3 to avoid duplicate work.

## D1 — Improve beginner setup instructions (easy)
Test the README on your actual operating system. Add Python/Git version checks,
how to locate the project folder, and commands matching the tested launcher.
Acceptance: a partner can run the app and tests from your instructions.

## R1 — Extract display formatting (medium)
Move a pure `format_task(task)` function into `team_tasks/formatting.py`.
Acceptance: exact existing output is preserved and tested for pending/completed
tasks; CLI remains responsible for printing. No unrelated feature changes.

## C1 — Practice a deliberate merge conflict (paired exercise)
Both people branch from the same main commit. Each replaces the exact sentence
under README's "Workshop description" heading with different wording.
Push and open both PRs before either is merged. Merge the first; the second
author merges origin/main, resolves the sentence collaboratively, tests, and
pushes. Acceptance: one agreed sentence, no markers, both contributions
acknowledged in the PR discussion. Details in WORKSHOP.md.

## Parallel assignment suggestions

For six pairs, start with B1, B2, B3, T1, D1, and R1. Each pair rotates author
and reviewer roles. Contributors touching tasks.py should keep edits focused;
different edits to one file do not necessarily produce conflicts. Give larger
features after the first round. Agree CLI option names before several pairs
modify cli.py. Use C1 for a predictable conflict instead of relying on chance.
