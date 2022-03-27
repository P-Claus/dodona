def common_characters(a, b):
    common_letters = ''
    count = 0
    for letter in b:
        if letter in a:
            if letter in common_letters:
                continue
            else:
                common_letters += letter
                count += 1
    return int(count)    

print(common_characters('bee', 'tween'))