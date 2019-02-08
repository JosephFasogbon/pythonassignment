def print_reverse(text, print_spaces=False):
    for letter in range(len(text), 0, -1):
        pad = ' ' * letter * print_spaces
        print(pad + text[letter-1])
print_reverse(text = "reversestring", print_spaces = True)

#printing without spaces

print_reverse(text = "reversestring")
