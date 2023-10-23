#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index method"""
        dataset = self.indexed_dataset()
        len_dataset = len(dataset)
        assert 0 <= index < len_dataset
        res_dict = {}
        data = []
        res_dict['index'] = index
        for i in range(page_size):
            while True:
                cur = dataset.get(index)
                index += 1
                if cur is not None:
                    break
            data.append(cur)

        res_dict['data'] = data
        res_dict['page_size'] = len(data)
        if dataset.get(index):
            res_dict['next_index'] = index
        else:
            res_dict['next_index'] = None
        return res_dict
