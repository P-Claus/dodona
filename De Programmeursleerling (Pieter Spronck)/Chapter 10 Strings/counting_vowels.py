text = "And now for something completely different."
txt = text.lower()
vowels = 'aeiou'

x = 0
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0


while x < len(txt):
   if txt[x] == vowels[0]:
      acount += 1
   if txt[x] == vowels[1]:
      ecount += 1
   if txt[x] == vowels[2]:
      icount += 1
   if txt[x] == vowels[3]:
      ocount += 1
   if txt[x] == vowels[4]:
      ucount += 1 
   x += 1

print('A:', acount)
print('E:', ecount)
print('I:', icount)
print('O:', ocount)
print('U:', ucount)
