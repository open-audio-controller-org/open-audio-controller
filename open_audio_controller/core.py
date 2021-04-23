"""
core.py provides audio I/O and passes to audio processing
"""

import logging
import struct
import time

import numpy as np
import pyaudio, wave, numpy

import open_audio_controller.module
import open_audio_controller.simple_filter

"""
Internal Debug Flag
"""
DEBUG = True

class module_core():
    """
    Constants holding user's desired settings.
    To be removed when replaced with JSON-based settings.
    """

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    READ_FROM_FILE = False
    RECORD_TO_FILE = False
    PLAYBACK_AUDIO = True
    RECORD_SECONDS = 5
    WAVE_INPUT_FILENAME = "../tests/test_core_audio_files/test_input.wav"
    WAVE_OUTPUT_FILENAME = "../tests/test_core_audio_files/test_output.wav"

    """
    Internal Global Variables
    """
    audio_engine = None
    audio_frames = []
    audio_stream = None
    audio_file = None
    processing_modules = []
    plot_data = None

    def __init__(self):
        self.audio_engine = pyaudio.PyAudio()
        self.processing_modules.append(open_audio_controller.simple_filter.module_simple_filter())


    def start_stream(self):
        """
            Starts audio stream.

            Parameters:
                ----------
                None

            Returns:
                ----------
                None
        """
        try:
            if self.READ_FROM_FILE:
                self.audio_file = wave.open(self.WAVE_INPUT_FILENAME, 'rb')
                self.RECORD_SECONDS = self.audio_file.getnframes()/ self.audio_file.getframerate()
                self.audio_stream = self.audio_engine.open(
                    format=self.audio_engine.get_format_from_width(self.audio_file.getsampwidth()),
                    channels=self.audio_file.getnchannels(),
                    rate=self.audio_file.getframerate(),
                    output=self.PLAYBACK_AUDIO,
                    input=False,
                    stream_callback=self.stream_callback)

            else:
                self.audio_stream = self.audio_engine.open(format=self.FORMAT,
                                                           channels=self.CHANNELS,
                                                           rate=self.RATE,
                                                           output=self.PLAYBACK_AUDIO,
                                                           input=True,
                                                           stream_callback=self.stream_callback)
            self.audio_stream.start_stream()
            return -1
        except Exception:
            return 0

    def stream_callback(self,
                        in_data: bytes,
                        frame_count: int,
                        time_info: dict,
                        flag: int) -> (numpy.ndarray, int):
        """
            Prepares audio engine.

            Parameters:
                ----------
                in_data : bytes
                    Input audio data from engine
                frame_count : int
                    Number of frames in input data
                time_info : dict
                    Dictionary containing loading, current, and finished timing
                flag : int
                    PortAudio callback flag


            Returns:
                ----------
                audio_data : numpy.ndarray
                    Output byte array
                pyAudio.paContinue : int
                    Internal signaling of whether there is more audio to process
        """

        if self.READ_FROM_FILE:
            in_data = self.audio_file.readframes(frame_count)

        audio_data = in_data

        plot_data = np.array(struct.unpack(str(2 * self.CHUNK) + 'B', audio_data), dtype='b')[::2]

        for enhancement in self.processing_modules:
            audio_data = enhancement.stream_callback(audio_data, frame_count, time_info, flag)

        if self.RECORD_TO_FILE:
            self.audio_frames.append(audio_data)

        return audio_data, pyaudio.paContinue

    def end_stream(self):
        """
            Ends live audio stream.

            Parameters:
                ----------
                None

            Returns:
                ----------
                None
        """
        self.audio_stream.stop_stream()
        if self.RECORD_TO_FILE: self.save_wave()
        return -1

    def save_wave(self):
        """
            Stores data in new wave file.

            Parameters:
                ----------
                None

            Returns:
                ----------
                None
        """
        wave_file = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wave_file.setnchannels(self.CHANNELS)
        wave_file.setsampwidth(self.audio_engine.get_sample_size(self.FORMAT))
        wave_file.setframerate(self.RATE)
        wave_file.writeframes(b''.join(self.audio_frames))
        wave_file.close()
        return -1

    def cleanup_engine(self):
        """
            Cleanup audio engine.

            Parameters:
                ----------
                None

            Returns:
                ----------
                None
        """
        if self.audio_stream is not None: self.audio_stream.close()
        if self.audio_engine is not None: self.audio_engine.terminate()
        return -1


def main():
    """
        Main function for testing

        Parameters:
            ----------
            None

        Returns:
            ----------
            None
    """
    if DEBUG:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

    test = module_core()
    test.start_stream()
    time.sleep(test.RECORD_SECONDS)
    test.end_stream()


if __name__ == "__main__":
    main()
