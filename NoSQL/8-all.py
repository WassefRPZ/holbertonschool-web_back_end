#!/usr/bin/python3
def list_all(mongo_collection):
    """list all documents"""
    data = mongo_collection.find()
    data_list = list(data)
    return data_list
