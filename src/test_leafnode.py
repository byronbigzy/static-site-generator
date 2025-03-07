import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Where are the tags?", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Where are the tags?")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError) as e:
            node.to_html()

        self.assertEqual(str(e.exception), "All leaf nodes must have a value.")
