from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Links"
    IMAGE = "Images"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        return self.text == other_node.text and \
        self.text_type.value == other_node.text_type.value and \
        self.url == other_node.url
    

    def __repr__(self):
        return f"TextNode('{self.text}', {self.text_type.value}, '{self.url}')"