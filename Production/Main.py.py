import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()

# --- 1. PIN CONFIGURATION ---
keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.row_pins = (board.D3, board.D6, board.D7) # UPDATE THESE to match your routing!
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- 2. ENCODER SETUP ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
# Pin A = D0, Pin B = D1 
encoder_handler.pins = ((board.D0, board.D1, None, False),)

# --- 3. OLED SETUP ---
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC, 1:["Layer"]},
        corner_two={0:OledReactionType.LAYER, 1:["1", "2"]},
        corner_three={0:OledReactionType.STATIC, 1:["Macropad"]},
        corner_four={0:OledReactionType.STATIC, 1:["v1.0"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)

# --- 4. KEYMAP  ---
# Layer 0: Productivity (Copy/Paste/Zoom)
# Layer 1: Media (Play/Pause/Volume)

# Define special keys
MO_1 = KC.MO(1) # Hold to switch to Layer 1

keyboard.keymap = [
    # LAYER 0: Productivity
    [
        KC.LGUI(KC.C),    KC.LGUI(KC.V),    KC.LGUI(KC.X),    # Copy, Paste, Cut
        KC.LGUI(KC.Z),    KC.LGUI(KC.S),    KC.F5,            # Undo, Save, Refresh
        KC.MUTE,          MO_1,             KC.LGUI(KC.L),    # Mute, Layer Shift, Lock Screen
    ],
    # LAYER 1: Media & Nav (Hold the center key in bottom row to access)
    [
        KC.MPRV,          KC.MPLY,          KC.MNXT,          # Prev, Play/Pause, Next
        KC.HOME,          KC.TRNS,          KC.END,           # Home, (Empty), End
        KC.VOLD,          KC.TRNS,          KC.VOLU,          # Vol Down, (Held), Vol Up
    ]
]

# --- 5. ENCODER MAP ---
# [Rotate Counter-Clockwise, Rotate Clockwise, Button Press]
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), # Layer 0: Volume & Mute
    ((KC.PGDN, KC.PGUP, KC.ENT),),  # Layer 1: Scroll Page & Enter
]

if __name__ == '__main__':
    keyboard.go()