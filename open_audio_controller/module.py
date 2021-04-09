from abc import ABC
import numpy


class module(ABC):



    def __init__(self):
        pass


    def processing_module(self,
                        in_data: bytes,
                        frame_count: int,
                        time_info: dict,
                        flag: int) -> (numpy.ndarray, int):
        return in_data