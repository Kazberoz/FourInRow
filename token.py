
class Token(object):
    def __init__(self,color):
        self._color=color
    
    def get_color(self):
        return self._color


if __name__ == "__main__":
    t=Token('x')
    print t.get_color()