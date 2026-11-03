"""KMK firmware for the XIAO RP2040 macropad.

The host_stats.py companion provides Linux PC statistics and handles volume /
brightness commands over CircuitPython's USB CDC data serial port.
"""
import json
import time

import board
import busio
import displayio
import i2cdisplaybus
import neopixel
import terminalio
import usb_cdc
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306
from kmk.consts import DiodeOrientation
from kmk.keys import KC, Key
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules import Module
from kmk.modules.encoder import EncoderHandler

# PCB pin mapping. See README for the complete table.
ROW_PINS = (board.D0, board.D1, board.D2)
COL_PINS = (board.D3, board.D6, board.D7)
ENCODER_A = board.D8
ENCODER_B = board.D9
PIXEL_PIN = board.D10
PIXEL_COUNT = 8

CLICK_WINDOW = 0.35
class HostBridge(Module):
    """USB messages, OLED pages, delayed single/double click, and RGB status."""
    def __init__(self):
        super().__init__()
        self.serial = usb_cdc.data
        self.rx_buffer = ""
        self.page = 0
        self.mode = "volume"
        self.pending_click_at = None
        self.pc = {"cpu": None, "ram": None, "temp": None}
        self.last_draw = 0
        self.last_pc_update = 0
        self.key_count = 0
        self.turn_count = 0
        self.last_action = "READY"
        self.pixels = neopixel.NeoPixel(
            PIXEL_PIN, PIXEL_COUNT, brightness=0.08, auto_write=False
        )
        self._start_oled()
        self.set_lights()
        self.draw_oled(force=True)

    def _start_oled(self):
        displayio.release_displays()
        self.i2c = busio.I2C(board.D5, board.D4)  # SCL, SDA on XIAO RP2040
        self.oled_bus = i2cdisplaybus.I2CDisplay(self.i2c, device_address=0x3C)
        self.display = SSD1306(self.oled_bus, width=128, height=32)
        self.group = displayio.Group()
        self.lines = [
            label.Label(terminalio.FONT, text="", x=0, y=7),
            label.Label(terminalio.FONT, text="", x=0, y=17),
            label.Label(terminalio.FONT, text="", x=0, y=27),
        ]
        for line in self.lines:
            self.group.append(line)
        self.display.root_group = self.group

    def send(self, message):
        if self.serial is None:
            return
        try:
            self.serial.write((json.dumps(message) + "\n").encode("utf-8"))
        except (OSError, ValueError):
            pass

    def encoder_turn(self, direction):
        self.turn_count += 1
        if self.mode == "volume":
            self.send({"type": "control", "mode": "volume", "direction": direction})
            self.last_action = "VOLUME UP" if direction > 0 else "VOLUME DOWN"
        else:
            self.send({"type": "control", "mode": "brightness", "direction": direction})
            self.last_action = "BRIGHTNESS UP" if direction > 0 else "BRIGHTNESS DOWN"
        self.set_lights()

    def button_released(self):
        now = time.monotonic()
        self.key_count += 1
        if self.pending_click_at is not None and now - self.pending_click_at <= CLICK_WINDOW:
            self.pending_click_at = None
            self.mode = "brightness" if self.mode == "volume" else "volume"
            self.last_action = "MODE: " + self.mode.upper()
            self.send({"type": "mode", "mode": self.mode})
            self.set_lights()
        else:
            self.pending_click_at = now

    def process_serial(self):
        if self.serial is None:
            return
        try:
            chunk = self.serial.read(64)
        except (OSError, ValueError):
            return
        if not chunk:
            return
        self.rx_buffer += chunk.decode("utf-8", "ignore")
        while "\n" in self.rx_buffer:
            line, self.rx_buffer = self.rx_buffer.split("\n", 1)
            try:
                message = json.loads(line)
                if message.get("type") == "stats":
                    self.pc = message
                    self.last_pc_update = time.monotonic()
            except (ValueError, AttributeError):
                pass

    def before_matrix_scan(self, keyboard):
        self.process_serial()
        now = time.monotonic()
        if self.pending_click_at is not None and now - self.pending_click_at > CLICK_WINDOW:
            self.pending_click_at = None
            self.page = (self.page + 1) % 2
            self.last_action = "DISPLAY PAGE " + str(self.page + 1)
            self.set_lights()
        if now - self.last_draw >= 0.25:
            self.draw_oled()

    def set_lights(self):
        if self.page == 1:
            color = (0, 90, 24)
        elif self.mode == "volume":
            color = (0, 35, 110)
        else:
            color = (110, 38, 0)
        for i in range(PIXEL_COUNT):
            self.pixels[i] = color
        self.pixels.show()

    def draw_oled(self, force=False):
        now = time.monotonic()
        self.last_draw = now
        if self.page == 0:
            stale = now - self.last_pc_update > 5
            cpu = "--" if stale or self.pc.get("cpu") is None else str(round(self.pc["cpu"]))
            ram = "--" if stale or self.pc.get("ram") is None else str(round(self.pc["ram"]))
            temp = self.pc.get("temp")
            temp_text = "--" if stale or temp is None else str(round(temp))
            text = ("PC DASHBOARD", "CPU " + cpu + "%  RAM " + ram + "%",
                    "TEMP " + temp_text + "C   " + self.mode.upper())
        else:
            phrase = ("MAKE IT CLICK", "KNOB WITH A PLAN", "TINY BOARD, BIG IDEAS")[(self.turn_count // 4) % 3]
            text = ("MACROPAD / " + self.mode.upper(), phrase[:21],
                    "KEYS " + str(self.key_count) + "  TURNS " + str(self.turn_count))
        for line, value in zip(self.lines, text):
            line.text = value[:21]

bridge = HostBridge()

def knob_button_on_press(key, keyboard, coord_int=None):
    pass

def knob_button_on_release(key, keyboard, coord_int=None):
    bridge.button_released()

KNOB_BUTTON = Key(on_press=knob_button_on_press, on_release=knob_button_on_release)

def volume_down(key, keyboard, coord_int=None):
    bridge.encoder_turn(-1)

def volume_up(key, keyboard, coord_int=None):
    bridge.encoder_turn(1)

ENCODER_LEFT = Key(on_press=volume_down)
ENCODER_RIGHT = Key(on_press=volume_up)

keyboard = KMKKeyboard()
keyboard.row_pins = ROW_PINS
keyboard.col_pins = COL_PINS
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = EncoderHandler()
encoder.pins = ((ENCODER_A, ENCODER_B, None, False),)
encoder.map = [((ENCODER_LEFT, ENCODER_RIGHT, KC.NO),)]
keyboard.modules = [encoder, bridge]

keyboard.keymap = [[
    KC.LCTL(KC.C),             # MX1: Copy
    KC.LCTL(KC.V),             # MX2: Paste
    KC.LCTL(KC.Z),             # MX3: Undo
    KC.LCTL(KC.X),             # MX4: Cut
    KC.LCTL(KC.S),             # MX5: Save
    KC.LALT(KC.TAB),           # MX6: App switch
    KC.HOME,                   # MX7: Home
    KNOB_BUTTON,               # EC11 push: single tap page / double tap mode
    KC.LCTL(KC.LSFT(KC.ESC)),  # MX8: system task manager shortcut
]]

if __name__ == "__main__":
    keyboard.go()
