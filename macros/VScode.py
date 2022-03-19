# MACROPAD Hotkeys example test  

from keyboard_layout_win_fr import KeyboardLayout
from keycode_win_fr import Keycode

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'VS Code', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Comment', [Keycode.CONTROL,Keycode.K,Keycode.C]),
        (0x000000, '', []),
        (0x004000, 'Uncomment', [Keycode.CONTROL, Keycode.K, Keycode.U]),
        
        #(0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x000000, '',[]),
        (0x000000, '',[]),
        (0x000000, '',[]),                  
        # 3rd row ----------
        (0x000000, '',[]),
        (0x000000, '',[]),
        (0x000000, '',[]),
        # 4th row ----------
        (0x000000, '',[]), 
        (0x000000, '',[]), 
        (0x000000, '',[]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'x']) # Close tab
    ]
} 
