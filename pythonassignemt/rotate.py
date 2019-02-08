def print_rotate(text, print_direction = 0):
    pad = ' ' * len(text)

    new_text = []

    counter = pad_counter = range(0, len(text), 1)

    limiter = 0

    n_pad = ''

    join_with = '\n'

    if print_direction >= 2 and print_direction <= 5:
        counter = range(len(text), 0, -1)
        limiter = 1

    if print_direction == 1 or print_direction == 3:
        pad_counter = range(len(text), 0, -1)

    if print_direction % 4 == 2:
        n_pad = '\n' * round(len(text)/2)
        join_with = pad = ''

    for letter in counter:
        if print_direction % 2 != 0: pad = ' ' * pad_counter[letter-limiter]
        new_text.append(pad + text[letter-limiter])

    print(n_pad + join_with.join(new_text))

for n in range(0, 8):
    print('\nDirection: ' + str(n) + '\n')
    print_rotate(text = "rotate", print_direction = 0)

    
