def print_rotate(word = 'rotate', direction=4):

    if (direction >= 1) and (direction <= 4):
                word = word[::-1]
                centering = 0

    if direction % 2 == 0:

        if direction % 4 == 0:
            for letter in word:
                print(' '*len(word) + letter)


        else:
            print(' '*centering + word)

    elif direction % 4 == 3:
        for i in rnage(0, len(word), 1):
            print(' '*(i+centering) + word[i])

    else:
        for i in range(len(word)-1, -1, -1):
            print(' '*(i+centering) + word[i])


for i in range(8):
          exec("print_rotate('rotate', direction=" + str(i) + ")")
