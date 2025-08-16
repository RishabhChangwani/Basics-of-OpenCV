#!/usr/bin/env python3

"""
Unit test for hello_world.py script.

This test checks if the script prints 'Hello, World!' correctly.
"""

import unittest
from io import StringIO
from unittest.mock import patch
import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_output(self) -> None:
        """
        Test the output of the hello_world script.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            hello_world.main()
            self.assertEqual(fake_out.getvalue().strip(), "Hello, World!")


if __name__ == '__main__':
    unittest.main()
