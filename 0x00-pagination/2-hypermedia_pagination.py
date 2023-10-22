#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return tuple of size two"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Returns requested page from the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_items = len(dataset)

        start_index, end_index = index_range(page, page_size)

        if start_index >= total_items:
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Returns a dictionary containing the following key-value pairs"""
        page_dict = {'page_size': 0, 'page': 0, 'data': 0,
                    'next_page': 0, 'prev_page': 0, 'total_pages': 0}
        page_dict['page'] = page
        page_dict['page_size'] = page_size
        page_dict['data'] = self.get_page()
        page_dict['next_page'] = page_dict['page'] + 1
        page_dict['prev_page'] = page_dict['page'] - 1
        
        dataset = self.dataset()
        total_pages = len(dataset)
        page_dict['total_pages'] = total_pages

        return page_dict
