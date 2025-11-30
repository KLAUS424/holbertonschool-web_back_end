#!/usr/bin/env python3
""" 9-insert_school.py """

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs for the document fields

    Returns:
        The _id of the newly inserted document.
    """
    if mongo_collection is None or not kwargs:
        return None

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
