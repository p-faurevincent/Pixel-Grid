from rpi_ws281x import Color

WHITE = Color(1, 1, 1)
RED = Color(20, 0, 0)
GREEN = Color(0, 20, 0)
BLUE = Color(0, 0, 20)
YELLOW = Color(20, 20, 0)
CYAN = Color(0, 20, 20)
PINK = Color(20, 0, 20)
VIOLET = Color(10, 0, 20)
ORANGE = Color(20, 10, 0)


class Pixel:
    def __init__(self, x, y, index, color = WHITE):
        self.x_value = x
        self.y_value = y
        self.index = index
        self.color = color


class Grid:
    def __init__(self, width, height, strip):
        self.width = width
        self.height = height
        self.pixels = []
        self.strip = strip
        index = 0
        for j in range(0, self.height, 1):
            for i in range(0, self.width, 1):
                y = j
                if j % 2 == 0 :
                    x = i
                else:
                    x = width - i - 1
                pixel = Pixel(x,y,index)
                self.pixels.append(pixel)
                #print("case {} : x={}, y={}".format(index, pixel.x_value, pixel.y_value))
                index = index + 1

    def _get_pixel_index(cls, x, y):
        if y % 2 == 0:
            index = x + y * cls.width
        else:
            index = cls.width - x - 1 + y * cls.width
        return index

    def set_pixel_color(self, x, y, color):
        self.pixels[self._get_pixel_index(x, y)].color = color

    def square(self, color, x=0, y=15):
        for i in range(16):
            for j in range(1):
                self.pixels[self._get_pixel_index(i+x, j+y)].color = color

    def clear(self):
        for i in range(256):
            self.pixels[i].color = WHITE

    def _clean_digit(cls):
        for j in range(5):
            for i in range(3):
                cls.pixels[cls._get_pixel_index(i,j)].color = WHITE

    def zero(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(0,0)].color = color
        self.pixels[self._get_pixel_index(0,1)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(0,3)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color
        self.pixels[self._get_pixel_index(1,0)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color

    def one(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color

    def two(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(0,0)].color = color
        self.pixels[self._get_pixel_index(1,0)].color = color
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(0,1)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(1,2)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def three(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(0,0)].color = color
        self.pixels[self._get_pixel_index(1,0)].color = color
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(1,2)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def four(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(1,2)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(0,3)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def five(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(0,0)].color = color
        self.pixels[self._get_pixel_index(1,0)].color = color
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(1,2)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(0,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def six(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(0,0)].color = color
        self.pixels[self._get_pixel_index(0,1)].color = color
        self.pixels[self._get_pixel_index(1,0)].color = color
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(1,2)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(0,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def seven(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def eight(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(0,0)].color = color
        self.pixels[self._get_pixel_index(0,1)].color = color
        self.pixels[self._get_pixel_index(1,0)].color = color
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(1,2)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(0,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def nine(self, color):
        self._clean_digit()
        self.pixels[self._get_pixel_index(0,0)].color = color
        self.pixels[self._get_pixel_index(1,0)].color = color
        self.pixels[self._get_pixel_index(2,0)].color = color
        self.pixels[self._get_pixel_index(2,1)].color = color
        self.pixels[self._get_pixel_index(0,2)].color = color
        self.pixels[self._get_pixel_index(1,2)].color = color
        self.pixels[self._get_pixel_index(2,2)].color = color
        self.pixels[self._get_pixel_index(2,3)].color = color
        self.pixels[self._get_pixel_index(0,3)].color = color
        self.pixels[self._get_pixel_index(2,4)].color = color
        self.pixels[self._get_pixel_index(1,4)].color = color
        self.pixels[self._get_pixel_index(0,4)].color = color

    def print(self):
        for pixel in self.pixels:
            self.strip.setPixelColor(pixel.index, pixel.color)
        self.strip.show()
