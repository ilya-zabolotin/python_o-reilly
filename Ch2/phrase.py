phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)
for i in range(4):
    plist.pop(7)
plist.remove('\'')
plist.insert(3, plist.pop(5))
plist.insert(4, plist.pop(5))
plist.insert(2, plist.pop(5))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
