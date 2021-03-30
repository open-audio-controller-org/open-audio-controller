"""
core.py provides audio I/O and passes to audio processing
"""

import logging
import time
import pyaudio, wave, numpy

"""
Constants holding user's desired settings.
"""

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
READ_FROM_FILE = False
RECORD_TO_FILE = False
RECORD_SECONDS = 5
WAVE_INPUT_FILENAME = "../tests/test_core_audio_files/test_input.wav"
WAVE_OUTPUT_FILENAME = "../tests/test_core_audio_files/test_output.wav"

"""
Internal Debug Flag
"""
DEBUG = True

"""
Internal Global Variables
"""
audio_engine = None
audio_frames = []
audio_stream = None
audio_file = None


def prepare():
    """
        Prepares audio engine.

        Parameters:
            ----------
            None

        Returns:
            ----------
            None
    """
    global audio_engine
    audio_engine = pyaudio.PyAudio()


def start_stream():
    """
        Starts audio stream.

        Parameters:
            ----------
            None

        Returns:
            ----------
            None
    """
    global audio_stream, audio_engine, audio_file
    if READ_FROM_FILE:
        audio_file = wave.open(WAVE_INPUT_FILENAME, 'rb')
        audio_stream = audio_engine.open(format=audio_engine.get_format_from_width(audio_file.getsampwidth()),
                                     channels=audio_file.getnchannels(),
                                     rate=audio_file.getframerate(),
                                     output=True,
                                     input=False,
                                     stream_callback=stream_callback)

    else:
        audio_stream = audio_engine.open(format=FORMAT,
                                     channels=CHANNELS,
                                     rate=RATE,
                                     output=True,
                                     input=True,
                                     stream_callback=stream_callback)
    audio_stream.start_stream()


def stream_callback(in_data: bytes,
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

    global audio_frames, audio_file
    if READ_FROM_FILE:
        audio_data = audio_file.readframes(frame_count)
    else:
        audio_data = numpy.frombuffer(in_data, dtype=numpy.float32)
    if RECORD_TO_FILE:
        audio_frames.append(audio_data)
    # logging.info(f"Typeof audio_data: {type(audio_data)}")
    # logging.info(f"Typeof continue: {type(pyaudio.paContinue)}")
    return audio_data, pyaudio.paContinue


def end_stream():
    """
        Ends live audio stream.

        Parameters:
            ----------
            None

        Returns:
            ----------
            None
    """
    audio_stream.stop_stream()
    if RECORD_TO_FILE: save_wave()


def read_wave():
    """
        Reads existing wave file.

        Parameters:
            ----------
            None

        Returns:
            ----------
            None
    """
    global audio_file

    pass


def save_wave():
    """
        Stores data in new wave file.

        Parameters:
            ----------
            None

        Returns:
            ----------
            None
    """
    global audio_engine, audio_frames
    wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio_engine.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(audio_frames))
    wave_file.close()


def cleanup_engine():
    """
        Cleanup audio engine.

        Parameters:
            ----------
            None

        Returns:
            ----------
            None
    """
    if audio_stream is not None: audio_stream.close()
    if audio_engine is not None: audio_engine.terminate()


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
    prepare()
    start_stream()
    time.sleep(RECORD_SECONDS)
    end_stream()
    cleanup_engine()


if __name__ == "__main__":
    main()
