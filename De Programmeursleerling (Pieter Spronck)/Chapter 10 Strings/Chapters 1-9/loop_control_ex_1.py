sum = 0

for i in ( 12, 4, 3, 33, -2, -5, 7, 22, 4 ):
    
    if i == 0:
        break
    if i < 0:
        continue
    sum += i

else: 
    print(sum)
        

print('Done')
