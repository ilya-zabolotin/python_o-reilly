phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3]) + ' ' + ''.join(plist[4:5]) + ''.join(plist[7:5:-1])

print(plist)
print(new_phrase)
