# MorseCoder-V2
Brand new morse coder with a twist.  
This program takes in plain text as an input, and then beebs out morse code.  

#### Morse code sound files are from Wikipedia:
`dot.ogg` file: https://upload.wikimedia.org/wikipedia/commons/e/e7/E_morse_code.ogg  
`dash.ogg` file: https://upload.wikimedia.org/wikipedia/commons/b/ba/T_morse_code.ogg  


To use the program, first install `pygame`. `pygame` is used to play the morse code sound files across platforms:  
```
pip install pygame
```
Then you can run `main.py` and pass in plain text to be translated into morse code:  
```
python main.py "sos"
```
The progam then beeps out the morse code along with this visual output:
```
... --- ...
```

## Brief `MorseCode` package documentation:
Import the `Morse` class from `MorseCode` package:
```python
from MorseCode.Coder import Morse
```
Then you can use the `encode()` and `decode()` methods:
```python
from MorseCode.Coder import Morse

plain_text = 'SOS'
morse_code = Morse.encode(plain_text) # Encodes 'SOS' to '... --- ...'

decoded_morse_code = Morse.decode(morse_code) # Decodes '... --- ...' to 'SOS'
```
### Use the `print_and_play()` method to print morse code onto the screen while beeping out the morse signals:
```python
from MorseCode.Coder import Morse
morse_code = Morse.encode(plain_text) # Encodes 'SOS' to '... --- ...'

Morse.print_and_play(morse_code) # Prints out '... --- ...' while beeping out a sequence of corresponding morse code signals.
```
