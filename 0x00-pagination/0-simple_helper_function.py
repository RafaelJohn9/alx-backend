#!/usr/bin/env python3
"""
a module that contains function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    a function that takes two integer arg page
    and page_size and returns a tuple of them
    """
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
