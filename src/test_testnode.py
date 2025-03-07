import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a google link", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a google link", TextType.LINK, "www.google.com")
        self.assertEqual(node, node2)

    def test_notEq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_notEq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "www.google.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, text, www.google.com)")
    

if __name__ == "__main__":
    unittest.main()