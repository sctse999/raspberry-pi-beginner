from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)

device = sh1106(serial, persist=True)
device.cleanup = None

font = ImageFont.truetype(
    '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 8)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((0, 0), "Hello World!", fill="white", font=font)

