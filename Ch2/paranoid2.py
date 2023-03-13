paranoid = "Ozzy, the Knight of Darkness"
letters = list(paranoid)
for char in letters[:5]:
    print('\t', char)
print()
for char in letters[-8:]:
    print('\t'*2, char)
print()
for char in letters[10:16]:
    print('\t'*3, char)
