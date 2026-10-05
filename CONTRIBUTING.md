# Contributing

Pick an issue and agree ownership with the instructor before coding. Keep one
issue per branch and pull request. Suggested names: `fix/empty-stats`,
`feature/csv-export`, `test/cli-errors`, `docs/windows-setup`.

## Shared-repository workflow

Replace OWNER and REPO with the instructor's repository details:

```sh
git clone https://github.com/OWNER/REPO.git
cd REPO
git switch main
git pull --ff-only origin main
git switch -c fix/empty-stats
```

Write a failing regression test, implement the change, then run all tests:

```sh
python -m unittest discover -s tests -v
git status
git diff
git add team_tasks/tasks.py tests/test_tasks.py
git diff --cached
git commit -m "Fix statistics for an empty task list"
git push -u origin fix/empty-stats
```

Stage the actual files you changed; the paths above are just an example.
Open a GitHub PR into `main`. Explain the problem, behavior, and tests.
Include `Closes #N` using the actual GitHub issue number (the task codes in
`docs/ISSUES.md` are not GitHub issue numbers). Request a peer review.

## Reviews and updates

Review for correct behavior, edge cases, readable names, focused scope, and
useful tests. Leave specific, respectful comments. The author addresses them
by committing and pushing again on the same branch. Wait for passing CI and
peer approval; the instructor performs the merge.

Before resolving a conflict, commit your own work. On your feature branch:

```sh
git fetch origin
git merge origin/main
```

If Git reports conflicts, edit each conflicted file into the intended final
version, remove conflict markers, stage the resolved files, run tests, and
commit the merge. Push the same branch. `git merge --abort` cancels an
in-progress merge if you need to start again. Do not force-push for this lesson.

After merging, switch to main and `git pull --ff-only origin main` before
creating a new branch. Do not reuse a merged branch for the next issue.

## Optional fork workflow

Without repository write access, fork on GitHub and clone your fork instead.
Add the instructor repository as upstream:

```sh
git remote add upstream https://github.com/OWNER/REPO.git
git fetch upstream
git switch main
git merge --ff-only upstream/main
git switch -c feature/my-change
```

Push to your fork's `origin`; open the PR against the instructor's `main`.
To update a feature branch, fetch upstream and merge `upstream/main`.
