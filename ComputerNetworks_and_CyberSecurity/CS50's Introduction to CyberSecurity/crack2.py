# This code generate all the 4 digit alphabet password
# Total possibilities 52 * 52 * 52 * 52

from string import ascii_letters

for thousands_place in ascii_letters:
    for hundreds_place in ascii_letters:
        for tens_place in ascii_letters:
            for ones_place in ascii_letters:
                print(thousands_place, hundreds_place, tens_place, ones_place)