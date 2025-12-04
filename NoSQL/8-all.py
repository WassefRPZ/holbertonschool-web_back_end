#!/usr/bin/pytho
"""first pymongo code"""

def list_all(mongo_collection):
    """list"""
    return mongo_collection.find()
