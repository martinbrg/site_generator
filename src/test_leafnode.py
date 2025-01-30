import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    
    def setUp(self):
        self.node = LeafNode("p", "hello world")  # Modify according to your class structure

    def test_no_value(self):
        """Test case when there’s no value"""
        self.node.value = None
        self.node.tag = "p"
        self.node.props = {"class": "bold"}
        
        with self.assertRaises(ValueError):
            self.node.to_html()

    def test_no_tag(self):
        """Test case when there’s no tag"""
        self.node.value = "Hello"
        self.node.tag = None
        self.node.props = {"class": "bold"}
        
        result = self.node.to_html()
        self.assertEqual(result, "Hello")

    def test_no_props(self):
        """Test case when there are no props"""
        self.node.value = "Hello"
        self.node.tag = "p"
        self.node.props = {}
        
        result = self.node.to_html()
        self.assertEqual(result, "<p>Hello</p>")

