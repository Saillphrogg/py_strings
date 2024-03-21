def reverse(text: str) -> str:
    return(text[::-1])
    pass

def first_to_upper(text: str) -> str:
    return ' '.join(word[0].capitalize if word[0].islower() else word for word in text.split())
    pass

def count_vowels(text: str) -> int:
    samo="aeiouAEIOU"
    ile=0
    for c in text:
        if c in samo:
            ile += 1
    return ile
    pass


def sum_digits(text: str) -> int:
    return sum(int(c) for c in text if c.isdigit())
    pass


def search_substr(text: str, sub: str) -> int:
    for i in range(len(text)-len(sub)+1):
    	if text[i:i+len(sub)]==sub:
    		return i
    return None
    pass




