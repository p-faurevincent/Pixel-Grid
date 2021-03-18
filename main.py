#!/usr/bin/env python3

import time
from rpi_ws281x import *
import argparse
import random

# LED strip configuration:
LED_COUNT      = 256     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


WHITE = Color(1,1,1)
RED = Color(20,0,0)
GREEN = Color(0,20,0)
BLUE = Color(0,0,20)
YELLOW = Color(20,20,0)
CYAN = Color(0,20,20)
PINK = Color(20,0,20)
VIOLET = Color(10,0,20)
ORANGE = Color(20,10,0)


class Pixel:
    def __init__(self, x, y, index, color = WHITE):
        self.x_value = x
        self.y_value = y
        self.index = index
        self.color = color


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []
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
    
    def _get_pixel_index(cls,x,y):
        if y % 2 == 0 :
            index = x + y * cls.width
        else:
            index = cls.width - x - 1 + y * cls.width    
        return index    
    
    def square(self, color, x=0, y=15):
        for i in range(16):
            for j in range(1):
                self.pixels[self._get_pixel_index(i+x,j+y)].color = color  
    
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



def color_wipe(strip, color=Color(0,0,0), wait_ms=1):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def print_grid(strip, grid):
    for pixel in grid.pixels:
        strip.setPixelColor(pixel.index, pixel.color)
    strip.show()


def randomize(strip, grid):
    for t in range(250):
        for j in range(16):
            for i in range(16):
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                color = Color(red, green, blue)
                grid.pixels[grid._get_pixel_index(i,j)].color = color
        print_grid(strip, grid)
        time.sleep(0.1)


def square_wipe(strip, grid, color=Color(12,5,5)):
    for j in range(8):
        for i in range(16):
            grid.pixels[grid._get_pixel_index(i,j)].color = color
            grid.pixels[grid._get_pixel_index(j,i)].color = color
            grid.pixels[grid._get_pixel_index(i,grid.height - j - 1)].color = color
            grid.pixels[grid._get_pixel_index(grid.height - j - 1,i)].color = color
        print_grid(strip, grid)
        time.sleep(0.01)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
        
    ma_grille = Grid(16,16)

    try:
        while True:
            ma_grille.square(Color(255,255,255))
            print_grid(strip, ma_grille)
            time.sleep(5)
            randomize(strip,ma_grille)
            square_wipe(strip, ma_grille, RED)
            square_wipe(strip, ma_grille, ORANGE)
            square_wipe(strip, ma_grille, YELLOW)
            square_wipe(strip, ma_grille, GREEN)
            square_wipe(strip, ma_grille, CYAN)
            square_wipe(strip, ma_grille, BLUE)
            square_wipe(strip, ma_grille, VIOLET)
            square_wipe(strip, ma_grille, PINK)
            square_wipe(strip, ma_grille, RED)
            square_wipe(strip, ma_grille, ORANGE)
            square_wipe(strip, ma_grille, YELLOW)
            square_wipe(strip, ma_grille, GREEN)
            square_wipe(strip, ma_grille, CYAN)
            square_wipe(strip, ma_grille, BLUE)
            square_wipe(strip, ma_grille, VIOLET)
            square_wipe(strip, ma_grille, PINK)
            ma_grille.zero(RED)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.one(BLUE)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.two(GREEN)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.three(YELLOW)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.four(CYAN)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.five(PINK)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.six(ORANGE)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.seven(CYAN)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.eight(CYAN)
            print_grid(strip, ma_grille)
            time.sleep(1)
            ma_grille.nine(CYAN)
            print_grid(strip, ma_grille)
            time.sleep(1)

    except KeyboardInterrupt:
        if args.clear:
            color_wipe(strip)
