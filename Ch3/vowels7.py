vowels = set('aeiou')
          
word = input("Provide a word to search for vowels: ")

i = vowels.intersection(set(word))

for vowels in i:
    print(vowels)
