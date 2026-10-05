# Instructor guide — 90-minute Git/GitHub workshop

## Before class

Learners need basic Python functions, lists, dictionaries, and terminal usage.
Verify Python 3.10+, Git, GitHub accounts, and working GitHub authentication
before the timed session. The app and tests need no external Python packages.
The archive contains source files, not an initialized Git repository.

Create an empty GitHub repository without an initial README, license, or
gitignore. Extract this project and run from its root:

```sh
git init -b main
git add .
git commit -m "Add Team Tasks workshop starter"
git remote add origin https://github.com/OWNER/REPO.git
git push -u origin main
```

Replace OWNER/REPO first. Make sure hidden `.github` and `.gitignore` files
remain present after extraction. Configure your own Git name/email if Git
asks; do not copy someone else's identity.

Give participants repository write access, or choose the fork workflow in
CONTRIBUTING.md. Create GitHub issues from docs/ISSUES.md and assign one per
pair. Suggested labels (create them if desired): bug, enhancement,
documentation, tests, good first issue. Avoid assigning the same issue twice.

Run the workflow once and confirm a green Tests check. Where repository
settings permit, require PR review and the test check before merging to main.
Otherwise enforce those rules as a workshop convention. Keep merging with
the instructor during the first session. CI configuration follows GitHub's
Python guide: https://docs.github.com/en/actions/tutorials/build-and-test-code/python

## Session schedule

| Minutes | Activity | Evidence of learning |
| --- | --- | --- |
| 0–10 | Demo app, explain repo/branch/commit/PR | Everyone runs app and tests |
| 10–20 | Clone, choose issue, create branch | Each pair has a focused branch |
| 20–40 | Reproduce bug or specify feature; test and implement | Small commits with useful messages |
| 40–50 | Push and open a PR linked to issue | PR describes behavior and validation |
| 50–65 | Review another pair's PR; address feedback | Specific review and follow-up commit |
| 65–75 | Inspect CI; instructor merges; everyone syncs | Updated local main |
| 75–85 | Run C1 merge-conflict exercise | Conflict resolved without force-push |
| 85–90 | Debrief and select next task | Learners explain the complete workflow |

## Intentional bugs and the testing lesson

The 10 starter tests pass. They intentionally leave three gaps: stats for an
empty list, whitespace-only titles, and case-insensitive search. These are
B1–B3. Do not fix them before class. Learners should first write a regression
test, see it fail locally, implement their fix, and rerun the complete suite.
Green tests show only that tested behavior passes, not that no bugs exist.
For a CI demonstration, optionally push the failing test on a draft PR and
then push the fix; do not merge the failing revision.

## Predictable conflict demonstration

1. Two participants sync main and create separate branches from that same commit.
2. Both edit only the same existing Workshop description sentence in README.
3. Both commit, push, and open PRs before either PR is merged.
4. Merge participant A's PR first.
5. Participant B runs `git fetch origin` then `git merge origin/main` on their branch.
6. B reads the conflict markers, discusses the intended sentence with A, and
   replaces the entire marked block with the agreed wording.
7. B runs tests, stages README, commits, and pushes. Review and merge B's PR.

In the fork workflow, use upstream/main instead. Check `git status` whenever
unsure which branch or merge state you are in. Keep this exercise separate
from feature work so learners can focus on the mechanics.

## Review prompts

- Can I reproduce the issue and verify the proposed behavior?
- Does a bug fix include a test that would fail on the old code?
- Are empty inputs, missing IDs, and persistence handled where relevant?
- Is this PR small enough to explain in a few sentences?
- Is the feedback actionable and respectful?

Success means every learner authors a change, reviews someone else's change,
sees CI, and syncs after a merge. For large groups, repeat the session with
features F1–F6. JSON storage is local to each participant: Git collaboration
shares the code, not a live shared task database.
