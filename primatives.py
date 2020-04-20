# primatives.py

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point x={self.x} y={self.y}'

class Shape():
    pass

class Line():
    """
    <svg height="210" width="500">
    <line x1="0" y1="0" x2="200" y2="200" style="stroke:rgb(255,0,0);stroke-width:2" />
    </svg>
    """
    def __init__(self,p1:Point,p2:Point):
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y
    
    def to_svg(self):
        return f'<line x1="{p1.x}" y1="{p1.y}" x2="{p2.x}" y2="{p2.y}" style="stroke:rgb(255,0,0);stroke-width:2" />'

    def __repr__(self):
        return f'Line from {p1} to {p2}'


class Quad(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point, p4:Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def to_svg(self):
        return f'<rect x="{self.p1.x}" y="{self.p1.x}" width="{self.p2.x-self.p1.x}" height="{self.p1.y-self.p4.y}" style="fill:blue;stroke:black;stroke-width:5;fill-opacity:0.1;stroke-opacity:0.9" />'

    def __repr__(self):
        return f'{self.p1}\n{self.p2}\n{self.p3}\n{self.p4}'