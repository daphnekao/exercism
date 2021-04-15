import unittest

from sgf_parsing import Node

class SgfParsingTest(unittest.TestCase):

    def test_node_without_properties(self):
        input_string = "(;)"
        expected = SgfTree()
        self.assertEqual(parse(input_string), expected)


if __name__ == "__main__":
    unittest.main()
