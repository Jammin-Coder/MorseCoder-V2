from MorseCode.Coder import Morse
import sys


input_text = sys.argv[1]

encoded_output = Morse.encode(input_text)
Morse.print_and_play(encoded_output)


# decoded_output = Morse.decode(input_text)
# print(decoded_output)


