import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):

        node = HTMLNode("link",
            "google", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"},
        )

        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"'
            )

    def test_notEq(self):

        node = HTMLNode("link",
            "google", 
            None, 
            {"href": "https://www.yahoo.com", "target": "_blank"},
        )

        node2 = HTMLNode("link",
            "google", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"},
        )

        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_repr(self):
        node = HTMLNode("link",
            "google", 
            ["child1", "child2"], 
            {"href": "https://www.google.com", "target": "_blank"},
        )

        self.assertEqual(repr(node), f"HTMLNode({node.tag}, {node.value}, Children: {node.children}, {node.props})")
    