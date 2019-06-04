#Jack Roach
#Using selection, iteration, function calls/parameters, inverting keys and values of associative arrays to translate morse code.


morse_letters = {     'B': '-...', 'C': '-.-.', 'G': '--.', 'H': '....', 'D': '-..',
                      'F': '..-.', 'M': '--',   'N': '-.',  'J': '.---', 'K': '-.-',
                      'L': '.-..', 'P': '.--.', 'Q': '--.-','R': '.-.',  'V': '...-',
                      'W': '.--',  'X': '-..-', 'S': '...', 'T': '-',    'Y': '-.--',
                      'Z': '--..', ' ': '/'
                      }

morse_vowels = {      'A': '.-', 'E': '.', 'I': '..', 'O': '---', 'U': '..-'
                      }

morse_numbers = {     '0': '-----',  '1': '.----',  '2': '..---', '3': '...--',
                      '4': '....-',  '5': '.....',  '6': '-....', '7': '--...',
                      '8': '---..',  '9': '----.'
                      }

inverseMorseLetters=dict((y,x) for (x,y) in morse_letters.items())


def decoder(code, positionInString = 0):

    if positionInString < len(code):
        morseLetter = ""
        for key,char in enumerate(code[positionInString:]):
            if char == " ":
                positionInString = key + positionInString + 1
                letter = inverseMorseLetters[morseLetter]
                return letter + decoder(code, positionInString)
            else:
                morseLetter += char
    else:
        return ""
   
def morse_original(morse_letters):
    return (morse_letters)

def morse_extended(morse_letters, morse_vowels):
    morse_extended = morse_letters.copy()
    morse_extended.update(morse_vowels)
    morse_extended_alphabetical = sorted(morse_extended.items())
    return (morse_extended_alphabetical)

def morse_ReverseNumbers(morse_numbers):
    morse_numbers_reversed = {y:x for x,y in morse_numbers.items()}
    morse_numbers_reversed = sorted(morse_numbers_reversed.items(), key = lambda t: t[1])
    return (morse_numbers_reversed)
        

print ("\nOrignal List of Morse-Code:")
print (morse_original(morse_letters))
print ("\nUpdated List of Morse-Code(With Vowels):")
print (morse_extended(morse_letters, morse_vowels))
print ("\nMorse Numbers (morse first, numbers second):")
print (morse_ReverseNumbers(morse_numbers))
print ("\nRecieving Incomming Message: \n.-- .... -.-- / .-.. -.-- -. -..- / -.-. .-. -.--")
print ("Translated:")
print (decoder(".-- .... -.-- / .-.. -.-- -. -..- / -.-. .-. -.-- ", positionInString = 0))