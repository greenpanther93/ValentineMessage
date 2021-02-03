#import json
#import logging
#import math
#from pathlib import Path
#import os
#from os import environ
#import sys
#import textwrap
#import time

#from PIL import Image, ImageFont, ImageDraw
#import lib.epd2in13_V2

logging.info("Display type: Waveshare")

    
display = lib.epd2in13_V2.EPD()
display.init(display.FULL_UPDATE)
display.Clear(0xFF)
# These are the opposite of what InkyPhat uses.
WIDTH = display.height # yes, Height
HEIGHT = display.width # yes, width
BLACK = "black"
WHITE = "white"
img = Image.new('1', (WIDTH, HEIGHT), 255)

draw = ImageDraw.Draw(img)

logging.info("Display dimensions: W %s x H %s", WIDTH, HEIGHT)