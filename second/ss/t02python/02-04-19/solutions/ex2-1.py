#!/usr/bin/env python
"""
converts a string of bits to a decimal integer.
"""

#use raw_input to get user's input on keyboard
bstring = raw_input("Enter a string of bits:")
decimal = 0

exponent = len(bstring)-1

#loop here for each bit in the binary
#tips: for looping within bstring you could use
#"for ... in bstring" or use index of the string
# you could use conversion formula below
# ** means to the power of ( for this it would be  [int(digit)*2]^exponent)
# decimal = decimal + int(digit) *2 ** exponent

for digit in bstring:
    decimal = decimal*2 + int(digit)

print decimal
#
# if str(type(decimal)) == "<type 'int'>":
#     print " the integer value is ", decimal
# else:
#     print  "Not string of bits"
#     print  bstring
