""" This module runs unittests in a python script """

import unittest
from io import StringIO

from app.model_test import ModelTest

def run_tests():
    ''' Run the unittests '''
    output = StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelTest)
    unittest.TextTestRunner(stream=output,verbosity=2).run(suite)
    result = output.getvalue().replace('\n', '<br />')
    output.close()
    return result