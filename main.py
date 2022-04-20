from MorseCode.Coder import Morse
import sys

"""
Morse code sound files are from Wikipedia.
Dot: https://upload.wikimedia.org/wikipedia/commons/e/e7/E_morse_code.ogg
Dash: https://upload.wikimedia.org/wikipedia/commons/b/ba/T_morse_code.ogg
"""

chars = sys.argv[1]
encoded = Morse.encode(chars)

Morse.print_and_play(encoded, rate=0.5)

        

