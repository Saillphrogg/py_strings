def reverse(text: str) -> str:
    """
    reverse the text and return it
    """
    return text[::-1]

def first_to_upper(text: str) -> str:
    """
    split the text and if the first leter is lower then capitalize it
    """
    return ' '.join([word[0].upper()+word[1:] for word in text.split()])

def count_vowels(text: str) -> int:
    """
    create vowels string
    crete an intiger counting value
    for char in text
        if char in vowels:
            counting+=1
    return counting
    """
    samo="aeiouyąęóAEIOUYĄĘÓ"
    ile=0
    for c in text:
        if c in samo:
            ile += 1
    return ile


def sum_digits(text: str) -> int:
    """
    return the sum of c ion text if c is a digit
    """
    return sum(int(c) for c in text if c.isdigit())


def search_substr(text: str, sub: str) -> int:
    """
    for i in range lenght of text - lenght of substring + 1
        if the section of the string starting from i to lenght of substring == substring
            return i
    else return None
    """
    for i in range(len(text)-len(sub)+1):
        if text[i:i+len(sub)]==sub:
            return i
    return None
