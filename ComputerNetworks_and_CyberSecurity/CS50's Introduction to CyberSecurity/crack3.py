# This code generate all the 4 digit mixture of alphabet + numeric + punctuation  password
# Total possibilities 94 * 94 * 94 * 94 

from string import ascii_letters, digits, punctuation

for thousands_place in ascii_letters + digits + punctuation:
    for hundreds_place in ascii_letters + digits + punctuation:
        for tens_place in ascii_letters + digits + punctuation:
            for ones_place in ascii_letters + digits + punctuation:
                print(thousands_place, hundreds_place, tens_place, ones_place)