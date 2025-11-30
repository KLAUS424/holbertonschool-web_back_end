#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic.
"""
from typing import List, Dict, Any


def schools_by_topic(mongo_collection: Any, topic: str) -> List[Dict[str, Any]]:
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for within the 'topics' array field.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries (school documents) that
        contain the specified topic in their 'topics' array.
    """
    # Find documents where the 'topics' array contains the specific 'topic' string.
    # MongoDB handles searching within arrays naturally:
    # db.school.find({ 'topics': 'Python' })
    schools = mongo_collection.find({"topics": topic})
    # Convert the cursor results to a list and return it
    return list(schools)
