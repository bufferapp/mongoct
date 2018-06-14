# mongoct

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[![PyPI version](https://badge.fury.io/py/mongoct.svg)](https://badge.fury.io/py/mongoct)

MongoDB [Change Streams](https://docs.mongodb.com/manual/changeStreams/) tracker. Using `mongoct` allows you to pipe the MongoDB collection changes to another program or file.

## Installation

To install `mongoct`, simply run:

```bash
$ pip install mongoct
```

## Quickstart

Before executing the command line tool you'll need a MongoDB URI connection in your environment (`MONGODB_URI`)¹.

Tracking changes in a certain collection is as easy as running the following command:

```bash
$ mongoct company posts
```

Changes will start flowing as JSON at the same time they're applied to the `post` collection in the `company` database.

You can now pipe the data to another program like [`jq`](https://stedolan.github.io/jq/) or save it to a file for latter processing.

¹ It's also possible to specify the MongoDB URI as an argument (`mongoct company posts "mongodb://user:pass@host/db"`)
