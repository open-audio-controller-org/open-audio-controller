"""core.py provides audio I/O and passes to audio processing"""

import time
import pyaudio, wave, numpy

"""These to be replaced with user's settings"""
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_TO_FILE = False
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

audio_engine = None
audio_frames = []
audio_stream = None

"""Setup PyAudio"""


def prepare():
    global audio_engine
    audio_engine = pyaudio.PyAudio()


"""Live Audio Input Record"""


def start_stream():
    global audio_stream, audio_engine
    audio_stream = audio_engine.open(format=FORMAT,
                                     channels=CHANNELS,
                                     rate=RATE,
                                     output=True,
                                     input=True,
                                     stream_callback=stream_callback)
    audio_stream.start_stream()


"""Functionality for active stream"""


def stream_callback(in_data, frame_count, time_info, flag):
    global audio_frames
    audio_data = numpy.fromstring(in_data, dtype=numpy.float32)
    if (RECORD_TO_FILE):
        audio_frames.append(audio_data);
    return audio_data, pyaudio.paContinue


"""Live Audio Input Stop"""


def end_stream():
    audio_stream.stop_stream()


"""File Audio Input Functionality"""


def read_wave():
    pass


"""File Audio Output Functionality"""


def save_wave():
    wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio_engine.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(audio_frames))
    wave_file.close()


"""Cleans up the audio engine"""


def cleanup_engine():
    if audio_stream is not None: audio_stream.close()
    if audio_engine is not None: audio_engine.terminate()


"""Main for Testing"""


def main():
    prepare()
    start_stream()
    time.sleep(10)
    end_stream()
    cleanup_engine()


if __name__ == "__main__":
    main()
