#!/usr/bin/env python3
"""first code in a MongoDB collection"""


def schools_by_topic(mongo_collection, topic):
    """find collection"""
    return mongo_collection.find({"topics": topic})
