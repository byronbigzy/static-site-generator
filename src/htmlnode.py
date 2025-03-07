class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""

        attributes = ""
        for key in self.props:
            attributes += (f' {key}="{self.props[key]}"')
        
        return attributes

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, Children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return f'{self.value}'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children is None:
            raise ValueError("All pparent nodes must have at least one child.")
        return f'<{self.tag}></{self.tag}'