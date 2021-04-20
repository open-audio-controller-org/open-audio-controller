import numpy


class module_abstract():

    def __init__(self):
        pass


    def stream_callback(self,
                        in_data: bytes,
                        frame_count: int,
                        time_info: dict,
                        flag: int) -> (numpy.ndarray, int):
        return in_data