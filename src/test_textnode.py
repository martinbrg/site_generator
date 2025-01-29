import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        #testing neq, using the default url parameter as trigger
        node = TextNode("This is a text node", TextType.BOLD, "www.example.org")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
            # Create a TextNode instance
            node = TextNode(
                text="Hello, world!",
                text_type=TextType.BOLD,
                url="http://example.com"
            )
            
            # Expected representation
            expected_repr = "TextNode('Hello, world!', Bold text, 'http://example.com')"
            
            # Assert that the __repr__ output matches the expected value
            self.assertEqual(repr(node), expected_repr)

class TestTextType(unittest.TestCase):
    def test_access_by_name(self):
        # Verify access by member name
        self.assertEqual(TextType["NORMAL"], TextType.NORMAL)
        self.assertEqual(TextType["BOLD"], TextType.BOLD)

    def test_access_by_value(self):
        # Verify access by member value
        self.assertEqual(TextType("Normal text"), TextType.NORMAL)
        self.assertEqual(TextType("Bold text"), TextType.BOLD)

    def test_enum_members(self):
        # Verify all members are present
        expected_members = {
            "NORMAL": "Normal text",
            "BOLD": "Bold text",
            "ITALIC": "Italic text",
            "CODE": "Code text",
            "LINK": "Links",
            "IMAGE": "Images",
        }
        actual_members = {member.name: member.value for member in TextType}
        self.assertEqual(actual_members, expected_members)

    def test_enum_values(self):
        # Verify that values are as expected
        self.assertEqual(TextType.NORMAL.value, "Normal text")
        self.assertEqual(TextType.BOLD.value, "Bold text")
        self.assertEqual(TextType.ITALIC.value, "Italic text")
        self.assertEqual(TextType.CODE.value, "Code text")
        self.assertEqual(TextType.LINK.value, "Links")
        self.assertEqual(TextType.IMAGE.value, "Images")




if __name__ == "__main__":
    unittest.main()