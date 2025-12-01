#!/usr/bin/env python3

def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.
    page: current page number (1-indexed)
    page_size: number of items per page
    Returns a tuple (start, end)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
