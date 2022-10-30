# End to end tests

## Initialize

Create some test data in the database:

- Create a namepace named `testns`
- Create in the `testns` namespace a user named `testuser` with a password `testuserpwd`

## Server

Install the server:

```bash
cd example
pip install -r requirements.txt
```

Configure the server:

```bash
export FLASK_APP=server.py
export QUID_DEMO_KEY=the_key_of_testns
```

## Test

Install:

```bash
cd tests
yarn
# install the playwright stuff
npx playwright install
```

Run:

```bash
yarn runtest
```