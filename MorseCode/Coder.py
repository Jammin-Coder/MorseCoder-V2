from .utils import *
import os
import threading
import pygame
import time

pygame.mixer.init()

class MorseAudio:
    def __init__(self, thread, char):
        self.char = char
        self.thread = thread

    def play(self):
        self.thread.start()
    
    def stop(self):
        self.thread.join()


class Morse:
    dirname = os.path.dirname(__file__)

    dot_sound_file = os.path.join(dirname, 'resources/dot.ogg')
    dash_sound_file = os.path.join(dirname, 'resources/dash.ogg')

    morse_map_path = os.path.join(dirname, 'resources/morse.json')
    morse_map = read_json(morse_map_path)


    @staticmethod
    def encode(plain_text):
        plain_text = plain_text.strip().upper()
        encoded_text = ''
        words = plain_text.split(' ')

        for word in words:
            morse_word = ''

            for char in word:
                encoded_char = get_dict_keys_by_value(Morse.morse_map, char)
                morse_word += encoded_char + ' '
            
            encoded_text += morse_word + '  '
        
        return encoded_text.strip()
    
    @staticmethod
    def decode(morse_string):
        decoded_text = ''
        morse_words = morse_string.split('  ')

        for morse_word in morse_words:
            morse_letters = morse_word.split(' ')

            for morse_char in morse_letters:
                decoded_char = Morse.morse_map[morse_char]
                decoded_text += decoded_char

            decoded_text += ' '
        
        return decoded_text.strip()
    

    @staticmethod
    def print_and_play(morse_str, rate=0.5):
        output_buffer = ''
        morse_sequence = []

        morse_words = morse_str.split('  ')
        for morse_word in morse_words:
            morse_char_groups = morse_word.split(' ')

            for morse_char_group in morse_char_groups:
                for char in morse_char_group:
                    if char == '.':
                        sound_file = Morse.dot_sound_file
                    
                    elif char == '-':
                        sound_file = Morse.dash_sound_file
                    
                    output_buffer += char
                    audio_thread = threading.Thread(target=Morse.audio_print, args=[sound_file, output_buffer])
                    morse_audio = MorseAudio(audio_thread, char)
                    morse_sequence.append(morse_audio)
                
                output_buffer += ' '
                morse_sequence.append(' ')
            
            output_buffer += '  '
            morse_sequence.append('  ')
    
        
        for i, morse_audio_char in enumerate(morse_sequence):
            if i == len(morse_sequence) - 2:
                break
            

            if type(morse_audio_char) != str:
                morse_audio_char.play()
                time.sleep(rate)
            
            elif morse_audio_char == ' ':
                time.sleep(rate * 1.3)
            
            elif morse_audio_char == '  ':
                time.sleep(rate * 1.5)
        

        for morse_audio_char in morse_sequence:
            if type(morse_audio_char) != str:
                morse_audio_char.stop()
        
        
        print()


    @staticmethod
    def audio_print(sound_file, output_buffer):
        print(output_buffer, end='\r')
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

                    