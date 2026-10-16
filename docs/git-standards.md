# Git standards

How a change gets into Prop Loft. If you're contributing, this is how we work; if you think a rule is wrong, open an issue and say why.

## Branch names

`type/short-description`, where the type is `feat`, `fix`, `docs`, or `chore`. Example: `feat/item-search`.

**Why:** the type tells a reviewer what kind of review a branch needs before they open it: a `docs/` change gets read for clarity, a `feat/` change gets run. We don't put issue numbers in branch names because the pull request links the issue, and the number adds nothing a reviewer can use.

## Commit messages

The [seven rules](https://cbea.ms/git-commit/): a subject line of 50 characters or fewer, in the imperative ("Add item search," not "Added item search"), and a body that explains *why* when the change isn't obvious.

**Why:** the history is the project's memory. A year from now, `git log` is how someone finds out why the checkout code works the way it does, and "fixed stuff" answers nothing. We considered a type prefix (Conventional Commits) and decided against it: we squash on merge, so the pull request title becomes the commit on `main`, and the branch name already carries the type.

## Pull requests

One logical change per pull request, small enough to review in one sitting. The description says what problem it solves (with `Closes #N` when there's an issue), the approach, where a reviewer should look first, and how you tested it.

**Why:** a reviewer who has to untangle three changes reviews none of them well. Small pull requests get reviewed sooner, and they're easier to revert when something goes wrong.

## Review

Every change goes through a pull request, including the maintainer's own.

- **A contributor's pull request** is reviewed by the maintainer before it merges.
- **The maintainer's own pull request** gets a written self-review against the template's checklist, posted as a comment on the pull request. Prop Loft has one maintainer right now, so this is the honest version of review, and we say so rather than pretend otherwise.
- **Once there's a second maintainer,** every change needs one approval from someone who didn't write it.

**Why:** review catches mistakes, but it also spreads knowledge of the code. A self-review is weaker on both counts. Writing it down in the pull request at least makes the check visible and keeps the habit in place for when a second reviewer arrives.

## Merging

Squash and merge. The maintainer merges, and the branch is deleted afterward.

**Why:** squashing gives `main` one commit per change, each of which can be read or reverted on its own. The step-by-step commits aren't lost; they stay on the pull request. We considered merge commits, which keep every branch commit on `main`, but on a project this size they make the history harder to read without telling us anything the pull request doesn't.

## Definition of done

A change is done when:

- [ ] it was reviewed under the rules above,
- [ ] it's merged to `main`,
- [ ] the tests pass on `main` (`python manage.py test`),
- [ ] the docs say what the code now does, if behavior changed, and
- [ ] its issue is closed, with a note if the result differs from what the issue asked for.

**Why:** "done" without a definition means "done on my machine." Each item is something a later contributor would otherwise have to discover was skipped.
