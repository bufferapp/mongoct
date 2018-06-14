# mongoct

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

MongoDB Change Streams tracker.

## Installation

To install `mongoct`, simply run:

```bash
$ pip install mongoct
```

## Quickstart

Before executing the command line tool you'll need a MongoDB URI connection in your environment (`MONGODB_URI`).

Tracking changes in a certain collection is as easy as running the following command:

```bash
$ mongoct company posts
```

Changes will start flowing as they're applied to the `post` collection in the `company` database.

Alternatively, you can also specify the MongoDB URI as an argument:

```bash
$ mongoct company posts "mongodb://user:pass@host/db"
```
