e A list in Python is just an ordered collection of items which can be of any type.
By comparison, an array is an ordered collection of items of the "same" type.

A list in Python is like an array in Perl.
A list in python is much more than array in Java and is more like the ArrayList class which can hold arbitrary objects and can expand dynamically as new items are added.

```
>>> li = ["a", "b", "peanut", "sausage"]

//First we defined a list of five string elements.

>>> li
['a', 'b', 'peanut', 'sausage']

// They retain their original order.

>>> li[0]
'a'

// A list can be used like a zero-based array. The first element of any non-empty array is 0.

>>> li[4]
'example'

//The last element of the five-element list is li[4] because lists are always zero-based.
```


A integer is a number without  decimal point : 1, 2, 47. -98
Decimal integers are integers expressed in decimal notation (base 10) and use the digits from 0 to 9 rather than binary or other integers

Each digit in a binary number is called a bit.
The subscript 2 denotes a binary number.

The number 1010110 is represented by 8 bits



The numbers system based on ones and zeroes is called the <i>bi</i>nary system (because there are only two possible digits.)
The <i>dec</i>imal system (ten possible digits 0-9) needs to be recapped as it would be easier to understand.

12510 = 1*100 + 2*10 + 5*1 = 1*10^2 + 2*10^1 + 5*10^0

The subscript 10 dnotes the number as a base 10 (decimal) number.
To see how many digits a nuber needs, you can take the logarithm( base 10) of the absolute value of the number and add 1 to it.
The integer part of the result is the number of digits.
( For example: log(base 10)(33) + 1 = 2.5
The integer part of that is 2, so 2 digits are needed.)
