#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
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
        """Get hyper index"""
        assert type(index) == int and type(page_size) == int\
            and index > 0 and page_size > 0
        assert index <= len(self.indexed_dataset())
        dataset = self.indexed_dataset()
        # print(dataset.keys())
        data = []
        next_index = index + page_size
        i = index
        while i < next_index:
            if i in dataset.keys():
                data.append(dataset[i])
            else:
                next_index += 1
            i += 1
        # for i in range(index, index + page_size):
        #     # print(i)
        #     data.append(self.indexed_dataset()[i])
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
