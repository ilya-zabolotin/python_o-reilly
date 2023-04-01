def search4vowels ():
    """Printing vowels from a provided word"""
    vowels = set('aeiou')
    word = input('Providea word to search for vowels: ')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
