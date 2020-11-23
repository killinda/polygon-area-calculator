class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height =  height
    def set_width(self,width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        self.result =""
        if self.width > 50 or self.height >50:
            return "Too big for picture."
        else:
            for row in range(self.height):
                self.result += "*"*(self.width)+"\n"
        return self.result       

    def get_amount_inside(self,object):
        return int(self.width/object.width)*int(self.height/object.height)
    def __str__(self):
        return "Rectangle(width=" + str(self.width)+", height=" + str(self.height)+")"

class Square(Rectangle):
    def __init__(self,length):
        self.width =length
        self.height=length
    def set_side(self,length):
        self.width = length
        self.height = length
    def set_width(self,width):
        self.width = width
        self.height = width
    def __str__(self):
        return "Square(side=" + str(self.width)+")"  



