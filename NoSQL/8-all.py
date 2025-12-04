#!/usr/bin/python3
from pymongo import MongoClient
"""first pymongo code"""

def list_all(mongo_collection):
    """list"""
    return list(mongo_collection.find())
