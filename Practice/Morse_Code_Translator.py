
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
    result = ""
    for letter in text:
        letter = letter.upper()