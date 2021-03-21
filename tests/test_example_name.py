import unittest
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
        self.val_a = 1
        self.val_b = 1

    def test_example_equality(self):
        '''
        The other functions declared within the class are your tests
        which will be comprised of self.assert* type calls, passing
        the appropriate parameters and a meaningful failure message.
        '''
        self.assertEqual(self.val_a, self.val_b,
                         "This would be displayed if the test failed")

    def tearDown(self):
        '''
        The opposite of setUp(), tearDown() can be used to deallocate
        resources which generally won't be necessary unless testing
        things with connection streams which require explicitly calling
        some form of .close() method.
        '''
        pass


"""
if __name__ == '__main__':
    '''
    The tests in this file will automatically be discovered and
    run in a suite by the main test file, but these tests can be run on their
    own by including this ifmain, which calls unittest.main() and simply
    running this file.
    '''
    unittest.main()
"""
