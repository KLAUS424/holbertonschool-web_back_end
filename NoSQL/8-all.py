#!/usr/bin/env python3
""" 8-all.py """

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents in the collection.
        Returns an empty list if the collection has no documents.
    """
    if mongo_collection is None:
        return []

    # Find all documents and convert cursor to list
    return list(mongo_collection.find())
