from . import ILI9341
from . import config


class EPD(object):
    def __init__(self):
        self.reset_pin = config.RST_PIN
        self.dc_pin = config.DC_PIN
        self.width = 320
        self.height = 240
        self.ILI9341 = ILI9341.ILI9341(config.spi, config.RST_PIN, config.DC_PIN, config.BL_PIN)

    def init(self):
        self.ili9341.Init()

    def clear(self):
        self.ili9341.clear()

    def display(self, image):
        rgb_im = image.convert('RGB')
        self.ili9341.ShowImage(rgb_im, 0, 0)
