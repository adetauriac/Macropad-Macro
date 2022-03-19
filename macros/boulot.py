# MACROPAD Hotkeys example test  

from keyboard_layout_win_fr import KeyboardLayout
from keycode_win_fr import Keycode

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Boulot', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'EPIC', [Keycode.ALT,Keycode.CONTROL,Keycode.J]),
        (0x004000, 'Board', [Keycode.ALT, Keycode.CONTROL, Keycode.W]),
        (0x004000, 'Compo', [Keycode.ALT, Keycode.CONTROL, Keycode.C]),
        #(0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, 'Size -', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x202000, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x400000, 'Mute', [Keycode.ALT,Keycode.CONTROL,Keycode.M]),                     # Mute
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000040, 'Home', [Keycode.ALT, Keycode.HOME]),
        (0x000040, 'Private', [Keycode.CONTROL, Keycode.N]),
        # 4th row ----------
        (0x800000, 'CtrlC', [Keycode.CONTROL, Keycode.C]), 
        (0x800000, 'CtrlV', [Keycode.CONTROL, Keycode.V]),  
        (0x101010, 'Hacks', [Keycode.CONTROL, Keycode.N, -Keycode.COMMAND,'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'x']) # Close tab
    ]
} 