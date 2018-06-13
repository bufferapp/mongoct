import click
import pymongo
from bson import json_util


@click.command()
@click.argument("database", type=str)
@click.argument("collection", type=str)
@click.argument("mongodb_uri", envvar="MONGODB_URI", type=str)
def run(database, collection, mongodb_uri):
    client = pymongo.MongoClient(mongodb_uri)
    db = client.get_database(database)
    col = db.get_collection(collection)
    cursor = col.watch(full_document="updateLookup")

    with cursor as stream:
        for change in stream:
            click.echo(json_util.dumps(change))


if __name__ == "__main__":
    run()
