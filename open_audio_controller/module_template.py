import numpy


class module_template:

    def __init__(self):
        pass

    def module_processor(self,
                         in_data: numpy.ndarray,
                         frame_count: int,
                         time_info: dict,
                         flag: int) -> (numpy.ndarray, int):
        return in_data
