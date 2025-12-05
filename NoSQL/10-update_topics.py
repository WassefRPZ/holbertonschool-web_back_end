#!/usr/bin/env python3
"""first code in a MongoDB collection"""


def update_topics(mongo_collection, name, topics):
    """update collection"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
