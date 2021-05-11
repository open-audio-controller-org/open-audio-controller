import sys
sys.path.insert(1, '/app/open_audio_controller')

import open_audio_flask

import unittest
"""
Mandatory import for unit testing capability
The code you want to test should also be imported here.
"""


class FlaskTests(unittest.TestCase):
    """
    Use a class which extends unittest.TestCase to
    group your tests together.
    """

    def setUp(self):
        """
        setUp() is used to declare variables or initialise data
        structures to be used across the test group.
        """
        self.open_audio_flask = open_audio_flask.test_client()
        open_audio_flask.config['TESTING'] = True
        open_audio_flask.config['WTF_CSRF_ENABLED'] = False
        open_audio_flask.config['DEBUG'] = False

    def recorder(self, state):
        return self.open_audio_flask.post('/controller_state', json={'state': state})

    def playback(self, state):
        return self.open_audio_flask.post('/playback', json={'state': state})

    def test_activating_recorder(self):
        """
        The other functions declared within the class are your tests
        which will be comprised of self.assert* type calls, passing
        the appropriate parameters and a meaningful failure message.
        """
        response = self.recorder(self, True)
        print(f"active_record {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_deactivating_module(self):
        response = self.recorder(self, False)
        self.assertEqual(response.status_code, 200)

    def test_activating_playback(self):
        response = self.playback(self, True)
        self.assertEqual(response.status_code, 200)

    def test_deactivating_module(self):
        response = self.playback(self, False)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """
        The opposite of setUp(), tearDown() can be used to deallocate
        resources which generally won't be necessary unless testing
        things with connection streams which require explicitly calling
        some form of .close() method.
        """
        pass



if __name__ == '__main__':
    """
    The tests in this file will automatically be discovered and
    run in a suite by the main test file, but these tests can be run on their
    own by including this ifmain, which calls unittest.main() and simply
    running this file.
    """
    unittest.main()
