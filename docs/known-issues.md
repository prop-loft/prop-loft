# Known issues

What's broken, unfinished, or deliberately cut in Prop Loft right now, so you don't have to find out the hard way. Every entry says what happens, when it affects you, what to do in the meantime, and the issue where the work is tracked.

The maintainer updates this file in the same pull request that fixes or adds an entry. If you hit something that isn't here, it's a gap in this list: [file a bug](https://github.com/prop-loft/prop-loft/issues/new?template=bug_report.yml).

*Last reviewed: November 2026.*

## Open bugs

**The catalog is too small to read on a phone.** The page has no viewport tag, so phone browsers lay it out at desktop width and shrink it. *Affects:* anyone opening the catalog on a phone. *Meanwhile:* pinch to zoom, or turn the phone sideways. *Tracked in:* [#31](https://github.com/prop-loft/prop-loft/issues/31), a good first issue.

## Temporary shortcuts

These are stand-ins, built only so the app could be used before the real thing exists. Don't build on them.

**Items and bins can only be added in the Django admin.** That needs a superuser account on the server, so it's a developer's tool, not a volunteer's. *Affects:* anyone adding stock. *Meanwhile:* use the admin, as in [step 8 of the setup guide](setup.md#8-optional-add-some-items). *Replaced by:* the add-item form, [#26](https://github.com/prop-loft/prop-loft/issues/26).

**There's no sign-in, and no roles.** Anyone who can reach the server can see the catalog; only the admin asks for a password. *Affects:* any deployment. *Meanwhile:* run Prop Loft only on your own machine. Don't put it on a server that others can reach yet. *Replaced by:* roles for the wardrobe lead and volunteers, [#17](https://github.com/prop-loft/prop-loft/issues/17).

**The pages have no styling.** They're plain HTML on purpose: the first milestone is about working, not looking finished (see the [roadmap](roadmap.md#now-the-mvp)). *Replaced by:* the phone-first layout, [#17](https://github.com/prop-loft/prop-loft/issues/17).

## Deliberate cuts

Decisions to leave something out, written down so nobody mistakes them for oversights.

**Plain forms, not HTMX.** Every page reloads in full when you submit a form. HTMX would make that smoother, but it didn't fit the first milestone's hours. *Why, and what would bring it back:* [design §6](design.md#decision-plain-forms-for-the-mvp-htmx-later). It's revisited after the strike-night trial.

**Roles, the phone layout, and running it at a theater come after the MVP.** These are the last two of the design's five milestones ([design §8](design.md#8-implementation-plan)). When we counted the hours one maintainer actually has this term, they didn't fit. They aren't dropped; they're what comes next. *Tracked in:* [#17](https://github.com/prop-loft/prop-loft/issues/17) and [#18](https://github.com/prop-loft/prop-loft/issues/18), with the reasoning in the [roadmap](roadmap.md#now-the-mvp).

## Not yet checked

Things that should work but that nobody has verified yet.

**Nothing has run on PostgreSQL.** Production is meant to use PostgreSQL ([design §6](design.md#decision-postgresql-for-the-database)), and the settings support it through `DATABASE_URL`. But the tests and the setup guide use SQLite, and no one has run the app on PostgreSQL. *Affects:* the first deployment. *Tracked in:* [#18](https://github.com/prop-loft/prop-loft/issues/18), running it at the theater.

**The tests run only when someone remembers to run them.** There's no continuous integration yet. The pull request template asks you to run `python manage.py test` before you push, and reviewers have to take your word for it. *Tracked in:* [#32](https://github.com/prop-loft/prop-loft/issues/32), open for help.

**iPhone photos may not display.** iPhones save photos as HEIC, which many browsers can't show. Photos aren't built yet, so this can't affect you today. It's listed because it's the design's biggest open risk for the feature ([design §7](design.md#7-risks-and-open-questions)). *Tracked in:* [#28](https://github.com/prop-loft/prop-loft/issues/28).
