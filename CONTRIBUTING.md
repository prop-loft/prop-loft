# Contributing to Prop Loft

Thanks for looking. Prop Loft is small and early, so a single contribution makes a visible difference, and you don't have to be a Django expert to make one. Fixing a confusing sentence, reporting a bug clearly, or telling us what your theater would need are all real contributions.

## Your first contribution

1. **Get oriented.** Read the [README](README.md), then skim the [design document](docs/design.md), at least the goals and non-goals. That's what the project is for and what it deliberately isn't.
2. **Find something to work on.** Issues labeled [`good first issue`](https://github.com/prop-loft/prop-loft/labels/good%20first%20issue) are scoped for someone new to the code. If none are open, look for [`help wanted`](https://github.com/prop-loft/prop-loft/labels/help%20wanted), or tell us what you'd like to do in a new issue. The [project board](https://github.com/prop-loft/prop-loft/projects) shows what's in progress, and the [roadmap](docs/roadmap.md) shows what's coming and where bigger contributions fit.
3. **Say you're taking it.** Comment on the issue, so two people don't do the same work. If you stop, say that too; it's fine.
4. **Set up the project** by following [Running it locally](README.md#running-it-locally) in the README. If any step fails, that's a bug in our instructions: file it.
5. **Make the change and open a pull request.** Opening a draft early to ask "am I on the right track?" is welcome.

## Other ways to help

- **Report a bug** with the [bug report form](https://github.com/prop-loft/prop-loft/issues/new?template=bug_report.yml). Steps to reproduce, and what you expected versus what happened, are what make a report fixable.
- **Suggest a feature** with the [feature request form](https://github.com/prop-loft/prop-loft/issues/new?template=feature_request.yml). Tell us the problem and who has it, even if you have no idea how to solve it.
- **Plan work** with the [task form](https://github.com/prop-loft/prop-loft/issues/new?template=task.yml), once it's decided: the goal, where it comes from, and the acceptance criteria that say when it's done. Most tasks are written by a maintainer, often by turning an accepted feature request into one.
- **Improve the docs.** If something here confused you, you're the best person to fix it, because you know exactly where it went wrong.
- **Review a pull request.** Reading someone else's change and asking a good question is a contribution too.

## Making a change

The full rules, with the reasons for each, are in our [git standards](docs/git-standards.md). The short version:

- Branch from `main` as `type/short-description` (`feat/`, `fix/`, `docs/`, `chore/`).
- Write commit messages that follow [the seven rules](https://cbea.ms/git-commit/), and say *why* in the body.
- Keep each pull request to one logical change, and fill in the template: the problem, your approach, where to look first, and how you tested it.
- Run the tests before you push: `python manage.py test`.
- The maintainer reviews, then merges with squash and merge.

## What to expect from review

You'll get a first review within one week. Reviews ask questions and suggest changes; that's the process working, not a verdict on you. Answer each comment, or push a change and say what you did. The full set of response times, and how decisions get made, are in our [communication norms](docs/communication-norms.md).

## Labels

| Label | Means |
|---|---|
| `needs triage` | New, and not yet read by a maintainer. Applied automatically by the issue forms. |
| `bug` | Something doesn't work as it should. |
| `enhancement` | A new feature or an improvement. |
| `documentation` | Docs only. |
| `epic` | A piece of user-visible value too big for one pull request. Its sub-issues are the work; it closes when they do. |
| `good first issue` | Scoped for someone new to the code, with a pointer to where to start. |
| `help wanted` | The maintainer would welcome someone taking this. |
| `question` | A question, not a change. |

## Licensing your contribution

Prop Loft is licensed under the [Apache License 2.0](LICENSE). By opening a pull request, you agree that your contribution is licensed under it too (the license's section 5 says this already; we're saying it plainly).

**Why Apache 2.0.** We want any theater, school, or company to be able to run Prop Loft, change it, and host it for others, including for a fee, without asking us first. That's a permissive license. Among permissive licenses we chose Apache 2.0 over MIT for two reasons: it includes an explicit patent grant, so every contributor licenses any patents covering their contribution to everyone who uses it, and it requires modified files to say they were changed, so a theater running a modified copy can tell what's ours. We considered a copyleft license like the GPL, which would keep every modified copy open. But our users are volunteer-run theaters and the people who help them, not software vendors, and a copyleft license would give them obligations to understand before they could adapt it. For this project, wide, easy adoption matters more than keeping every copy open.

## Code of conduct

Everyone taking part in Prop Loft agrees to follow our [code of conduct](CODE_OF_CONDUCT.md). It also says how to report a problem privately.
