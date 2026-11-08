# This code generate all the 4 digit number password
# Total possibilities is 10 * 10 * 10 * 10

from string import digits

for thousands_place in digits:
    for hundreds_place in digits:
        for tens_place in digits:
            for ones_place in digits:
                print(thousands_place, hundreds_place, tens_place, ones_place)