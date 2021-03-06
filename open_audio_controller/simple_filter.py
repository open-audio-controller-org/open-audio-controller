import numpy
from scipy.signal import butter, lfilter
from open_audio_controller.module_template import module_template


class module_simple_filter(module_template):
    fs = 5000.0
    lowcut = 500.0
    highcut = 1250.0

    def __init__(self):
        super().__init__()
        pass

    def butter_bandpass(self,
                        order=5):

        nyq = 0.5 * self.fs
        low = self.lowcut / nyq
        high = self.highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def butter_bandpass_filter(self,
                               data,
                               order=5):
        b, a = self.butter_bandpass(order=order)
        y = lfilter(b, a, data)
        return y

    def module_processor(self,
                         in_data: numpy.ndarray,
                         frame_count: int,
                         time_info: dict,
                         flag: int) -> (numpy.ndarray, int):

        # The following line is commented pending proper implementation of the filter module.
        # out_data = self.butter_bandpass_filter(in_data)

        out_data = in_data

        return out_data
