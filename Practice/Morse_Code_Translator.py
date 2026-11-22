
def morse_code_translator(text):
    text = input("Enter text to translate to Morse code: ")
    dictionary = [
        ("A", ".-"), ("B", "-..."), ("C", "-.-."), ("D", "-.."), ("E", "."),
        ("F", "..-."), ("G", "--."), ("H", "...."), ("I", ".."), ("J", ".---"),
        ("K", "-.-"), ("L", ".-.."), ("M", "--"), ("N", "-."), ("O", "---"),
        ("P", ".--."), ("Q", "--.-"), ("R", ".-."), ("S", "..."), ("T", "-"),
        ("U", "..-"), ("V", "...-"), ("W", ".--"), ("X", "-..-"), ("Y", "-.--"),
        ("Z", "--..")
    ]
    for letter in text:
        for char, morse in dictionary:
            if letter.upper() == char:
                print(morse, end=" ")
                break
        else:
            print(" ", end=" ")  # Print space for unrecognized characters