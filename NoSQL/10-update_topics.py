#!/usr/bin/env python3
""" 10-update_topics.py """

def update_topics(mongo_collection, name, topics):
    """
    Update the 'topics' field of a school document based on its name.

    Args:
        mongo_collection: pymongo collection object
        name (str): the school name to update
        topics (list of str): the list of topics to set

    Returns:
        The result of the update operation
    """
    if mongo_collection is None or not name:
        return None

    result = mongo_collection.update_one(
        {"name": name},       # filter by school name
        {"$set": {"topics": topics}}  # set the new topics list
    )

    return result
