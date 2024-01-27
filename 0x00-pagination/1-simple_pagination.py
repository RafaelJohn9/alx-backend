#!/usr/bin/env python3
"""
a module that contains function index_range
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) ->    Tuple[int, int]:
    """
    a function that takes two integer arg page
    and page_size and returns a tuple of them
    """
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)

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
        """
        paginates a dataset and gets it
        """
        # assertion operations
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        #import dataset
        dataset = self.dataset()

        # dataset pages and validation
        operation = len(dataset) / page_size
        dataset_pages = operation if isinstance(operation, int) else (len(dataset) // page_size) + 1
        if dataset_pages < page:
            return []

        # validates and get page
        page_range = index_range(page, page_size)
        start_index =  page_range[0]
        end_index = page_range[1]
        return dataset[start_index: end_index]
