import click
import pymongo
import logging
from bson import json_util


@click.command()
@click.argument("database", type=str)
@click.argument("collection", type=str)
@click.option("--uri", "-u", envvar="MONGODB_URI")
@click.option("--resume-token", "-r")
def run(database, collection, uri, resume_token):
    client = pymongo.MongoClient(uri)
    db = client.get_database(database)
    col = db.get_collection(collection)

    if resume_token:
        resume_token = json_util.loads(resume_token)
        cursor = col.watch(full_document="updateLookup", resume_after=resume_token)
    else:
        cursor = col.watch(full_document="updateLookup")

    with cursor as stream:
        for change in stream:
            click.echo(json_util.dumps(change))


if __name__ == "__main__":
    run()
