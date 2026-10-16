# Roadmap

Where Prop Loft is going, in order, and where you can help. The near term is tracked in [milestones](https://github.com/prop-loft/prop-loft/milestones) and on the [project board](https://github.com/prop-loft/prop-loft/projects); everything past them is here, with its [epic](https://github.com/prop-loft/prop-loft/issues?q=label%3Aepic) where one exists. The maintainer keeps this file current. If something here looks wrong or missing, open an issue and say so.

## Now: the MVP

Two milestones, each a slice a volunteer can use end to end:

| Milestone | What works when it closes |
|---|---|
| **M1 · Demo-able core** | Find an item by name, open its page, check it out to an actor for a show, and see it marked out. Items are entered through the admin; no photos, no styling. |
| **M2 · MVP complete** | Returns and the wardrobe lead's overdue list. A volunteer adds an item with a photo from a phone. Filters by category and size. |

**What we cut, and why.** The [design](design.md#8-implementation-plan) plans five slices before the strike-night trial. When we counted the hours one maintainer actually has this term, about 10 a week, two fit. Slices 4 and 5 are below, as the next things to build, not dropped.

## Next: ready for a real theater

These finish the design's MVP. They're the best places to make a large contribution, and each has an epic with its scope written down.

- **Roles and a phone-first layout.** What a volunteer can do versus the wardrobe lead, and every page laid out for a phone held in one hand. *Good for:* someone who knows Django's permission system, or someone who cares about mobile layout and accessibility.
- **Running it at the theater.** Deploy to the theater's own server, load the 60-item costume stock, and run a production's strike night on it. That trial is the real test of the design's goals. *Good for:* someone who has deployed a Django app before, and anyone who wants to help write the deployment guide.

## Later: beyond costumes

- **Props and set pieces.** The data model already allows any kind of item; the work is the categories, the fields each kind needs (a prop's fragility, a flat's dimensions), and search that copes with a much bigger stock.
- **More than one theater.** Today it's one deployment per theater ([design §6](design.md#decision-one-deployment-per-theater)). If several theaters run Prop Loft, an install guide a volunteer can follow without a developer becomes the most valuable thing in the repository.

## Not planned

The design's [non-goals](design.md#2-goals-and-non-goals) are out of scope on purpose: no ticketing or budgeting, no rental marketplace between theaters, no native app, no barcode hardware, no public catalog, and no notifications. Proposing one of these is welcome, but start with an issue that makes the case, because it changes what the project is.
