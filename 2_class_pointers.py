class Cookie:
    def __init__(self, color): # constructor, called when obj initialized
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color): # called normally to set color
        self.color = color
