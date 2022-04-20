import subprocess
import time
import threading
import os
from .utils import get_dict_key_by_value, read_json

class MorseChar:
    def __init__(self, thread, char):
        self.thread = thread
        self.char = char
    
    def play(self):
        self.thread.start()
    
    def stop(self):
        self.thread.join()


class Morse:
    # Set morse map to the morse.json file that is located in this directory.
    dirname = os.path.dirname(__file__) # Directory name of this file.

    # Path to sound files relitave to this directory.
    dot_sound_file = os.path.join(dirname,'resources/dot.ogg')  
    dash_sound_file = os.path.join(dirname,'resources/dash.ogg')
    # Path to morse code map file relitave to this directory.
    morse_map_file = os.path.join(dirname, 'resources/morse.json')

    # Read the map file and store the morse map in a dictionary.
    morse_map = read_json(morse_map_file)
    
    
    @staticmethod
    def morse_print(sound_file, output_buffer):
        """
        Print the current output_buffer and play the morse character's sound.
        """
        print(output_buffer, end='\r')
        subprocess.call(['paplay', sound_file])
    
    @staticmethod
    def print_and_play(morse_str, rate=0.2):
        """
        Prints out the morse_str 1 character at a time 
        and plays the character's corresponding sound.
        """
        output_buffer = '' # Used to store the current string of output characters.
        morse_sequence = [] # Used to store the sequence of morse characters and breaks.

        # Break up the provided morse code into seperate words
        for morse_word in morse_str.split('  '):

            # Break up the provided morse words into seperate character groups
            for morse_char_group in morse_word.split(' '):

                # Break up the character group into individual characters
                for char in morse_char_group:
                    if char == '.':
                        sound_file = Morse.dot_sound_file

                    elif char == '-':
                        sound_file = Morse.dash_sound_file
                    
                    output_buffer += char
                    thread = threading.Thread(target=Morse.morse_print, args=[sound_file, output_buffer])
                    morse_char = MorseChar(thread, char)
                    morse_sequence.append(morse_char)
                
                output_buffer += ' '
                morse_sequence.append(' ')

            output_buffer += '  '
            morse_sequence.append('  ')
        

        # Play the audio threads for the morse characters in the morse_sequence.
        for i, morse_char in enumerate(morse_sequence):
            # Stop the loop immediately if we've reached the end of the sequence of morse characters
            if i == len(morse_sequence) - 2:
                break
            
            # Play character sound
            if type(morse_char) != str:
                morse_char.play()
                time.sleep(rate)

            # If there is a space in characters, wait
            elif morse_char == ' ':
                time.sleep(rate * 1.3)
            
            # If there is a 2 space break in characters, wait longer.
            elif morse_char == '  ':
                time.sleep(rate * 1.5)

        # Stop the audio threads in the morse_sequence.
        for morse_char in morse_sequence:
            if type(morse_char) != str:
                morse_char.stop()
        print()

    @staticmethod
    def decode(string):
        string = string.upper()
        decoded_str = ''
        # Each morse word is seperated by 2 spaces.
        morse_words = string.split('  ')
        for word in morse_words:
            # Each morse letter is seperated by 1 space
            morse_letters = word.split(' ')
            for morse_char in morse_letters:
                decoded_char = Morse.morse_map[morse_char]
                decoded_str += decoded_char

            decoded_str += ' '
        return decoded_str

    @staticmethod
    def encode(string):
        string = string.strip().upper()
        encoded_str = ''
        words = string.split(' ')
        for word in words:
            morse_word = ''
            for char in word:
                if char != ' ':
                    encoded_char = get_dict_key_by_value(Morse.morse_map, char)
                    morse_word += encoded_char + ' '
            encoded_str += morse_word + ' '
        
        encoded_str = encoded_str.strip()
            
        return encoded_str
