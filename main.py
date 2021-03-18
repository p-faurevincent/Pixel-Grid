#!/usr/bin/env python3

import time
from rpi_ws281x import *
from Grid import *
import argparse
import random

# LED strip configuration:
GRID_WIDTH     = 16
GRID_HEIGHT    = 16
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def color_wipe(strip, color=Color(0,0,0), wait_ms=1):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def randomize(grid):
    for t in range(250):
        for j in range(16):
            for i in range(16):
                red = random.randint(0, 20)
                green = random.randint(0, 20)
                blue = random.randint(0, 20)
                color = Color(red, green, blue)
                grid.set_pixel_color(i, j, color)
        grid.print()
        time.sleep(0.1)


def square_wipe(grid, color=Color(12,5,5)):
    for j in range(8):
        for i in range(16):
            grid.set_pixel_color(i, j, color)
            grid.set_pixel_color(j, i, color)
            grid.set_pixel_color(i, grid.height - j - 1, color)
            grid.set_pixel_color(grid.height - j - 1, i, color)
        grid.print()
        time.sleep(0.01)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(GRID_WIDTH*GRID_HEIGHT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
        
    ma_grille = Grid(GRID_WIDTH, GRID_HEIGHT, strip)

    try:
        while True:
            square_wipe(ma_grille, RED)
            square_wipe(ma_grille, ORANGE)
            square_wipe(ma_grille, YELLOW)
            square_wipe(ma_grille, GREEN)
            square_wipe(ma_grille, CYAN)
            square_wipe(ma_grille, BLUE)
            square_wipe(ma_grille, VIOLET)
            square_wipe(ma_grille, PINK)
            square_wipe(ma_grille, RED)
            square_wipe(ma_grille, ORANGE)
            square_wipe(ma_grille, YELLOW)
            square_wipe(ma_grille, GREEN)
            square_wipe(ma_grille, CYAN)
            square_wipe(ma_grille, BLUE)
            square_wipe(ma_grille, VIOLET)
            square_wipe(ma_grille, PINK)
            ma_grille.zero(RED)
            ma_grille.print()
            time.sleep(1)
            ma_grille.one(BLUE)
            ma_grille.print()
            time.sleep(1)
            ma_grille.two(GREEN)
            ma_grille.print()
            time.sleep(1)
            ma_grille.three(YELLOW)
            ma_grille.print()
            time.sleep(1)
            ma_grille.four(CYAN)
            ma_grille.print()
            time.sleep(1)
            ma_grille.five(PINK)
            ma_grille.print()
            time.sleep(1)
            ma_grille.six(ORANGE)
            ma_grille.print()
            time.sleep(1)
            ma_grille.seven(CYAN)
            ma_grille.print()
            time.sleep(1)
            ma_grille.eight(BLUE)
            ma_grille.print()
            time.sleep(1)
            ma_grille.nine(YELLOW)
            ma_grille.print()
            time.sleep(1)

    except KeyboardInterrupt:
        if args.clear:
            color_wipe(strip)
