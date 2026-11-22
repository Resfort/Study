def morse_code_translator(text):
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

# Теперь запрос и вывод происходят снаружи:
user_input = input("Enter text to translate to Morse code: ")
translated = morse_code_translator(user_input)
print(translated)