#!/usr/bin/env python3
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.
    page: current page number (1-indexed)
    page_size: number of items per page
    Returns a tuple (start, end)
    """
    start = (page -1) * page_size 
    end = page * page_size
    return start, end

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0 
        assert isinstance(page_size, int) and page_size > 0 
            
        data = self.dataset()
        start, end = index_range(page, page_size)
        return data[start:end]
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
            
        data = self.get_page(page, page_size)
        page_size_res = len(data)
        dataset = self.dataset()
        total_item = len(dataset)
        total_page = math.ceil(total_item / page_size)
        if page < total_page and len(data) > 0:
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1 
        else:
            prev_page = None
        return {"page_size": page_size_res,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_page,
            }