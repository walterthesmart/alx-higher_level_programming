#!/usr/bin/python3
'#program that prints the ASCII alphabet, in lowercase, except q and e '

for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
