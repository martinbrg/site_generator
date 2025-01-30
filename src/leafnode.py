from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)


    def to_html(self):
        if not self.value:
            raise ValueError("Lead Nodes must have a value!")
        elif not self.tag:
            return self.value
        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
