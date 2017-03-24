import string

def alphabet_position(letter):
    letter = letter.lower()
    alphabet = string.ascii_lowercase
    return alphabet.index(letter)


def rotate_character(char, rot):
    alphabet = string.ascii_lowercase

    if not char.isalpha():
        return char

    new_index = alphabet_position(char) + rot

    if new_index >= 26:
        new_index = (new_index % 26)

    if char.isupper():
        return alphabet[new_index].upper()
    else:
        return alphabet[new_index]


def encrypt(text, rot):
    encrypted = ""
    rot = int(rot)
    for i in text:
        encrypted = encrypted + rotate_character(i, rot)
    return encrypted
