#!/usr/bin/env python3
"""
A Python function that changes all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes the 'topics' field for all school documents matching the given 'name'.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The name of the school document(s) to update.
        topics (list of str): The new list of topics to set for the school(s).
    """
    # The filter specifies which documents to update (matching the school name)
    filter_query = {"name": name}

    # The update operation uses the $set operator to replace the value
    # of the 'topics' field with the new list.
    update_operation = {"$set": {"topics": topics}}

    # update_many is used to ensure all documents matching the name are updated.
    mongo_collection.update_many(filter_query, update_operation)
