import numpy
from open_audio_controller.module import module_abstract


class module_simple_filter(module_abstract):


    def __init__(self):
        super().__init__()
        pass


    def stream_callback(self,
                          in_data: bytes,
                          frame_count: int,
                          time_info: dict,
                          flag: int) -> (numpy.ndarray, int):
        return in_data
