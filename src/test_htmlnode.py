import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_none(self):
        # Test when props is None
        obj = HTMLNode(props=None)
        result = obj.props_to_html()
        self.assertEqual(result, "")  # Expect an empty string

    def test_props_one_entry(self):
        # Test with a single entry in props
        obj = HTMLNode(props={"class": "button"})
        result = obj.props_to_html()
        self.assertEqual(result, ' class="button"')  # Expect the key-value pair formatted as HTML attributes

    def test_props_two_entries(self):
        # Test with multiple entries in props
        obj = HTMLNode(props={"class": "button", "id": "submit-button"})
        result = obj.props_to_html()
        # Since dictionaries don't guarantee order, check for either order
        expected1 = ' class="button" id="submit-button"'
        expected2 = ' id="submit-button" class="button"'
        self.assertIn(result, [expected1, expected2])  # Either order is acceptable
