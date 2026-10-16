# Communication and maintainer norms

Where Prop Loft talks, how quickly you can expect an answer, who maintains it, and how decisions get made. These are promises, so they're the ones we can keep.

## Where discussion happens

| You want to… | Go to |
|---|---|
| Report a bug | [An issue](https://github.com/prop-loft/prop-loft/issues/new/choose), using the bug report form |
| Suggest a feature | An issue, using the feature request form |
| Ask a question about the code or the design | An issue, labeled `question` |
| Discuss a specific change | The pull request's comments |
| Report a code of conduct problem | Privately, as described in the [code of conduct](../CODE_OF_CONDUCT.md). Never in a public issue. |

Everything else happens in public, in the issue tracker, so the next person with the same question can find the answer.

**There's no chat channel, on purpose.** With one maintainer, a chat channel is a promise of quick answers that we couldn't keep, and decisions made in chat are invisible to everyone who wasn't there. If that changes, this file will say so.

## What to expect, and when

| When you… | You can expect… |
|---|---|
| open an issue | it's read, labeled, and answered within **one week** |
| open a pull request | a first review within **one week** |
| reply to review comments | a response within **one week** of your reply |
| report a conduct problem | an acknowledgment within **one week** |

Prop Loft is maintained alongside a full-time teaching job. Expect slower answers during BYU's semester breaks and the last two weeks of each semester. If something you're waiting on has gone more than two weeks without an answer, comment on it to bump it; that's welcome, not rude.

## Who maintains Prop Loft

| Maintainer | What they do |
|---|---|
| Tom Stephens ([@dagorym](https://github.com/dagorym)) | Triages issues, reviews and merges pull requests, keeps the roadmap, and enforces the code of conduct |

**Becoming a maintainer.** After a few merged pull requests and some reviews of other people's, you're welcome to ask, in an issue. A second maintainer would change how review works: see [Review](git-standards.md#review) in the git standards.

## How decisions get made

- **Small changes** (a fix, a docs improvement, a feature already on the roadmap) are decided in the pull request. The maintainer approves it, asks for changes, or explains why not.
- **Bigger changes** (a new kind of feature, a new dependency, a change to the data model) start as an issue *before* any code. Describe the problem, not just the solution. The issue stays open for at least a week, so anyone interested can weigh in. The maintainer decides and writes the reason in the issue, and the [design document](design.md) is updated when the design changes.
- **Out of scope.** Features in the design's [non-goals](design.md#2-goals-and-non-goals) (ticketing, a rental marketplace, notifications, a native app) are closed with a link to that list. That isn't a judgment of the idea; it's how a small project stays finishable. If you think a non-goal should change, make that case in an issue.
- **Disagreement** is fine; say so in the issue or the pull request, with your reasons. The maintainer makes the final call and explains it. A decision can be reopened when there's new evidence.
