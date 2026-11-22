
def morse_code_translator(text):
    text = input("Enter text to translate to Morse code: ")
    morse_code = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--.."
    }
    result = ""
    for letter in text:
        letter = letter.upper()
        if letter in morse_code:
            result += f"{morse_code[letter]} "
        elif letter == " ":
            result += "/ "

    return result.strip()

print(morse_code_translator("SOS"))