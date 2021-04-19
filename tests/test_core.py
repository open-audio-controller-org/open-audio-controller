import time
import unittest
import open_audio_controller.core

'''
Mandatory import for unit testing capability
The code you want to test should also be imported here.
'''


class TestGroupName(unittest.TestCase):
    '''
    Use a class which extends unittest.TestCase to
    group your tests together.
    '''

    def setUp(self):
        '''
        setUp() is used to declare variables or initialise data
        structures to be used across the test group.
        '''
        self.core_test = open_audio_controller.core.module_core()

    def test_live(self):
        self.core_test.READ_FROM_FILE = False
        self.core_test.RECORD_TO_FILE = True
        self.core_test.WAVE_OUTPUT_FILENAME = "../tests/test_core_audio_files/test_output_live.wav"
        self.core_test.PLAYBACK_AUDIO = False
        self.assertEqual(-1, self.core_test.start_stream(), "Error in starting live stream()")
        time.sleep(2)
        self.assertEqual(-1, self.core_test.end_stream(), "Error in ending live stream()")

    def test_file(self):
        self.core_test.READ_FROM_FILE = True
        self.core_test.RECORD_TO_FILE = True
        self.assertEqual(-1, self.core_test.start_stream(), "Error in starting file stream()")
        self.core_test.WAVE_INPUT_FILENAME = "../tests/test_core_audio_files/test_input.wav"
        self.core_test.WAVE_OUTPUT_FILENAME = "../tests/test_core_audio_files/test_output_file.wav"
        self.core_test.PLAYBACK_AUDIO = False
        self.assertEqual(-1, self.core_test.end_stream(), "Error in ending file stream()")

    def tearDown(self):
        '''
        The opposite of setUp(), tearDown() can be used to deallocate
        resources which generally won't be necessary unless testing
        things with connection streams which require explicitly calling
        some form of .close() method.
        '''
        self.core_test.cleanup_engine()


if __name__ == '__main__':
    '''
    The tests in this file will automatically be discovered and
    run in a suite by the main test file, but these tests can be run on their
    own by including this ifmain, which calls unittest.main() and simply
    running this file.
    '''
    unittest.main()
