# VectorPad QMK Firmware
# Extras Rotary Encoder + SSD1306 OLED

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Keyboard definition
keyboard = KMKKeyboard()

# Matrix pins (from schematic)
# Columns: C1, C2, C3
keyboard.col_pins = (
    board.GP26,
    board.GP27,
    board.GP28,
)

# Rows: R1, R2, R3
keyboard.row_pins = (
    board.GP1,
    board.GP2,
    board.GP4,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Rotary Encoder
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Encoder A, B pins (from schematic)
encoder_handler.pins = (
    (board.GP8, board.GP9),
)

# Encoder push switch
encoder_handler.switch_pin = board.GP0

# Default encoder behavior (volume)
encoder_handler.map = [
    ((KC.VOLU,), (KC.VOLD,))
]

# OLED Display (SSD1306, I2C)
from kmk.extensions.display import Oled, Canvas

class LayerDisplay(Canvas):
    def __init__(self):
        super().__init__(128, 64)

    def draw(self, display):
        display.fill(0)
        display.text("VectorPad", 0, 0, 1)
        display.text("KMK Firmware", 0, 12, 1)
        display.text("Layer: BASE", 0, 32, 1)
        display.show()

oled_ui = LayerDisplay()

oled = Oled(
    width=128,
    height=64,
    i2c_num=1,
    sda=board.GP6,
    scl=board.GP7,
    display=oled_ui,
)

keyboard.extensions.append(oled)

# Keymap (3x3)
keyboard.keymap = [
    [
        KC.ONE, KC.TWO, KC.THREE,
        KC.FOUR, KC.FIVE, KC.SIX,
        KC.SEVEN, KC.EIGHT, KC.NINE,
    ]
]

# Main entry point
if __name__ == "__main__":
    keyboard.go()

