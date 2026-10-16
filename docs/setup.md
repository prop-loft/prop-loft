# Setting up Prop Loft for development

This guide takes you from nothing to a running copy of Prop Loft with its tests passing, in about fifteen minutes. Follow it in order. After the steps that can quietly go wrong, a **You should see** line tells you whether you're still on track.

If any step fails or confuses you, check [When a step fails](#when-a-step-fails). If your problem isn't there, that's a gap in this guide: please [file a bug](https://github.com/prop-loft/prop-loft/issues/new?template=bug_report.yml) and say which step.

## Prerequisites

| You need | Version | Check with | Install from |
|---|---|---|---|
| Python | 3.12 or newer | `python --version` | [python.org/downloads](https://www.python.org/downloads/) |
| Git | any recent version | `git --version` | [git-scm.com/downloads](https://git-scm.com/downloads) |

You don't need a database server. Local development uses a SQLite file that Django creates for you.

> **Windows:** the commands below work in PowerShell. Where a command differs, the Windows version is given next to it. If `python` isn't found, try `py` instead.

## Steps

### 1. Get the code

```sh
git clone https://github.com/prop-loft/prop-loft.git
cd prop-loft
```

If you plan to contribute, fork the repository on GitHub first and clone your fork instead.

### 2. Create a virtual environment and activate it

```sh
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
```

**You should see** `(.venv)` at the start of your prompt. Every command from here on assumes it's there. If you open a new terminal later, activate the environment again.

### 3. Install the dependencies

```sh
pip install -r requirements.txt
```

**You should see** a line starting `Successfully installed`, listing Django among other packages. A notice that a newer pip is available is harmless.

### 4. Create your settings file

```sh
cp .env.example .env               # Windows: copy .env.example .env
```

Open `.env` and replace `replace-with-a-long-random-string` with a real random value. This command prints one:

```sh
python -c "import secrets; print(secrets.token_urlsafe(40))"
```

Leave the other lines as they are. `.env` is ignored by git, so your key never gets committed.

### 5. Create the database

```sh
python manage.py migrate
```

**You should see** a list of migrations, each ending in `OK`, with `Applying catalog.0001_initial... OK` among them. This creates `db.sqlite3` in the project folder.

### 6. Run the tests

```sh
python manage.py test
```

**You should see** `Found 2 test(s).` near the top and, at the end:

```
Ran 2 tests in 0.007s

OK
```

The time will differ. The number of tests grows as the project does; what matters is the `OK`.

### 7. Start the server

```sh
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

**You should see** a page titled *Prop Loft — Catalog* that says **Nothing in the catalog yet**. That's correct: your database is empty. Stop the server with Ctrl+C.

### 8. Optional: add some items

To see the catalog with something in it, create an admin account and add a bin and a few items:

```sh
python manage.py createsuperuser
python manage.py runserver
```

Sign in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/), add a **Bin** (a label like `A-01` is enough), then add **Items** in that bin. Reload the catalog page and they're listed with their bins.

You're set up. Head back to [CONTRIBUTING.md](../CONTRIBUTING.md#your-first-contribution) to pick something to work on.

## When a step fails

**`KeyError: 'DJANGO_SECRET_KEY'`** at the end of a long error, on any `manage.py` command.
Django can't find your settings file. Make sure `.env` exists in the project folder, the one that contains `manage.py`, and not in a subfolder, and that its `DJANGO_SECRET_KEY` line has a value (step 4).

**`ModuleNotFoundError: No module named 'django'`** or **`'dotenv'`.**
Your virtual environment isn't active, so Python can't see the packages you installed. Activate it (step 2) and run the command again. If `(.venv)` is showing and you still get this, rerun step 3.

**On Windows: `running scripts is disabled on this system`** when you activate.
PowerShell blocks the activation script by default. Run this once, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**`python: command not found`,** or `python --version` shows 3.11 or older.
On macOS and Linux, try `python3`, and use `python3 -m venv .venv` in step 2. Once the environment is active, `python` works. On Windows, try `py`. If no version is 3.12 or newer, install one from python.org.

**`Error: That port is already in use.`** when you start the server.
Something else is using port 8000, often another copy of the server. Stop it, or run on a different port: `python manage.py runserver 8001`.

**`Bad Request (400)`** in the browser.
`DJANGO_DEBUG` or `DJANGO_ALLOWED_HOSTS` was changed in `.env`. For local development, set them back to the values in `.env.example`.
