def search4vowels (phrase: str) -> set:
    """Printing vowels from a provided word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters (phrase: str, letters: str='aeiou') -> set:
    """Return required letters from a provded phrase"""
    return set(letters).intersection(set(phrase))

