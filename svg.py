# svg.py

from primatives import Point, Quad

class SVG():
    def __init__(self, content):
        self.header = '<svg width="600" height="600">'
        self.body = content.to_svg()
        self.footer = '</svg>'

    def __repr__(self):
        return f'{self.header}\n{self.body}\n{self.footer}'
