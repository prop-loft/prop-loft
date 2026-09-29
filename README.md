# Prop Loft

Prop Loft is a catalog for the things a theater production keeps between shows. It helps a wardrobe lead and a crew of volunteers find an item, see where it's stored, and know who has it checked out. Version 1 covers costumes. The goal is every item a production stores: costumes, props, and set pieces.

> **A teaching project.** Prop Loft is the worked example for BYU's CS 301R, *Founding an Open-Source Project*. It's built in the open the way the course asks students to build theirs. The theater and the evidence cited in its design documents are invented for teaching.

**Status:** early. The [design](docs/design.md) is approved; the app lists items, and search is next.

## Why "Prop Loft" and not "Backstage"

The design started out under the name *Backstage*. When it came time to create this repository, we checked whether the name was free, and it wasn't: [Backstage](https://backstage.io) is Spotify's widely used open-source developer portal. Two projects sharing a name confuses searches, package names, and anyone trying to find either one. So this project is Prop Loft.

The new name is also deliberately broader than version 1. The design scopes costumes first, but the name is for where the project is going.

## Running it locally

You need Python 3.12 or newer.

```sh
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then set DJANGO_SECRET_KEY
python manage.py migrate
python manage.py runserver
```

Local development uses a SQLite file. Production uses PostgreSQL, selected by setting `DATABASE_URL`.

## Maintainers

- Tom Stephens ([@dagorym](https://github.com/dagorym))

## License

[Apache License 2.0](LICENSE)
