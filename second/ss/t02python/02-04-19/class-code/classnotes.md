# Types
```
a = 'this is a string'
if str(type(a)) == "<type 'str'>":
    print 'a string'
else:
    print 'not a string'
    print type(a)

```
comes out as `a string`
with
- a = 1.2
  - `not a string
      <type='float'>`
- a = 1
  - `not a string
      <type='int'>`

## String
A string is usually a bit of text you want to display to someone, or "export" out of the program you are writing. Python knows you want something to be a string when you put either `""` (double-quotes) or `''` (single-quotes) around the text.Also `"""` (triple-quoted strings) can be used to enclose blocks of text.  

Strings may contain the format characters you have discovered so far.
You simply put the formatted variables:
- %d = decimal number
- %s = string
- %r = "raw" data for the variable used for debugging.(Note: Meaning no formatting)

If you want to put multiple formats in your string to print multiple varaibles, you need to put them inside `()` parenthesis separated by `,` commas.


### Escapes
This `\` (backslash) character encodes difficult-to-type characters into a string. There are various "escape sequences" available for different characters you might want to use.
For example:

| ESCAPE      	| WHAT IT DOES. |
| ------------- |:-------------:|
|`\\`           |	Backslash (\)
|`\'`	          |Single-quote (')
|`\"`	          |Double-quote (")
|`\a`	          |ASCII bell (BEL)
|`\b`	          |ASCII backspace (BS)
|`\f`	          |ASCII formfeed (FF)
|`\n`	          |ASCII linefeed (LF) (meaning: line break)
|`\N`           |{name}	Character named name in the Unicode database (Unicode only)
|`\r`	          |Carriage Return (CR) (meaning: raw value)
|`\t`	          |Horizontal Tab (TAB)
|`\uxxxx`	      |Character with 16-bit hex value xxxx (Unicode only)
|`\Uxxxxxxxx`	  |Character with 32-bit hex value xxxxxxxx (Unicode only)
|`\v`	          |ASCII vertical tab (VT)
|`\ooo`	        |Character with octal value ooo
|`\xhh`	        |Character with hex value hh




An important escape sequence is to escape a single-quote `''` or double-quote `""`. Imagine you have a string that uses double-quotes and you want to put a double-quote inside the string. If you write `"I "understand" joe."` then Python will get confused because it will think the `"` around `"understand"` actually ends the string. You need a way to tell Python that the `""` inside the string isn't a real double-quote, but rather for display.

Example:
```
>>>"I \"understand\" Joe"
>I "understand" joe
```
or another avaliable solution would be to usse `"""` (triple-quotes) which works just like a string and you can put as many lines of text as you want until  you type `"""` again.
`'''` is also usable, and the only reason you might need both is if the string itself contains a triple quote.

```
line1 = '''This string contains """ so use triple-single-quotes.'''
line2 = """This string contains ''' so use triple-double-quotes."""
```

---
String class examples
```
>>> str_text = 'This is a string'
>>> len(str_text)
16
```
Shows the length of the string in characters
```
>>> str_text[0]
'T'
```
Shows the first object in array `[]`, which is zero-based, so is `T`

```
>>> str_text[-1]
'g'
```
Shows the last object in array `[]`, which goes back to `g`

```
>>> str_text[:]
'This is a string'
```
Refered to as slicing, and differs what it does depending on the `population`.
- If `population` is a **list**, this will create a new (shallow) copy of the list
- if `population` is a **tuple** or **str**, it will do nothing

It also acts as a limiter as with the following examples:

```
>>> str_text[1:]
'his is a string'
```
This will start the new (shallow) copy of the list from the second object as the starting is defined `[1:]`.
Keep in mind that the array `[]` is zero-based, so it starts on `h` not on `T`.

```
>>> str_text[1:4]
'his'
```
This will start the copy of the list from the second object, and end on 5th object in the array.

```
>>> str_text[:-2]
'This is a stri'
```
As array `[]` is zero-based, `[:-2]` will take out the last 2 objects in the array and copy the list.

```
>>> str_text[2:-2]
'is is a stri'
```
This is an array that starts out from the 3rd object with `[2:]` and ends with the last 2 objects taken out with `[:-2]`

```
>>> str_text.count('i')
3
```
Shows how many of a certain character there is in the string, for `'i'` there are 3 in the example.

```
>>> str_text.upper()
'THIS IS A STRING'
```
Returns the string in uppercase

```
>>> str_text
'This is a string'
```
Returns the string

---

## list

```
>>> list_var = [1, 2.3, 4, 'a string', 5, 1, 4, 5, 6, 'another string' , [2,3,"d"]]
>>> len(list_var)
11
>>> list_var[:0]
[]
>>> list_var[1]
2.3
>>> list_var[-1]
[2, 3, 'd']
>>> list_var[1:]
[2.3, 4, 'a string', 5, 1, 4, 5, 6, 'another string', [2, 3, 'd']]
>>> list_var[:-2]
[1, 2.3, 4, 'a string', 5, 1, 4, 5, 6]
>>> list_var.index(5)
4
>>> list_var.append(8)
>>> list_var[:]
[1, 2.3, 4, 'a string', 5, 1, 4, 5, 6, 'another string', [2, 3, 'd'], 8]
>>> list_var.extend([ 'some string', -6])
>>> list_var[:]
[1, 2.3, 4, 'a string', 5, 1, 4, 5, 6, 'another string', [2, 3, 'd'], 8, 'some string', -6]
>>> list_var
[1, 2.3, 4, 'a string', 5, 1, 4, 5, 6, 'another string', [2, 3, 'd'], 8, 'some string', -6]
>>> list_var.pop()
-6
>>> list_var
[1, 2.3, 4, 'a string', 5, 1, 4, 5, 6, 'another string', [2, 3, 'd'], 8, 'some string']
>>> list_var.remove(2.3)
>>> list_var
[1, 4, 'a string', 5, 1, 4, 5, 6, 'another string', [2, 3, 'd'], 8, 'some string']
>>> list_var.reverse()
>>> list_var
['some string', 8, [2, 3, 'd'], 'another string', 6, 5, 4, 1, 5, 'a string', 4, 1]
>>> list_var.sort()
>>> list_var
[1, 1, 4, 4, 5, 5, 6, 8, [2, 3, 'd'], 'a string', 'another string', 'some string
>>> for elmt in list_var:
... print elmt, list_var.index(elmt)
1 0
1 0
4 2
4 2
5 4
5 4
6 6
8 7
[2, 3, 'd'] 8
a string 9
another string 10
some string 11
```


## Set

```
>>> x = [1,2,3,4,5,6]
>>> set_var = set(x)
>>> set_var
set([1, 2, 3, 4, 5, 6])
>>> del(set_var)
>>> set_var
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'set_var' is not defined

>> x = [1,2,3,4,5,6]
>>> set_var = set(x)
>>> y = [23, 52, 59, 48]
set_var1 = set(y)
>>> set_var | set_var1
set([48, 1, 2, 3, 4, 5, 6, 23, 52, 59])
```

## Dictionary

```
dict_var = { 1: 2, 3 : 'a', 'b' : 4, 'c': 'd', 5 : 6, 'e' : [5, 6, 7] }
>>> len(dict_var)
6
>>> dict_var
{1: 2, 'c': 'd', 3: 'a', 'e': [5, 6, 7], 5: 6, 'b': 4}
>>> dict_var['f'] = 8
>>> dict_var
{1: 2, 'c': 'd', 3: 'a', 'e': [5, 6, 7], 5: 6, 'f': 8, 'b': 4}
>>> dict_var['d'] = {'x':20, 'y' : 21}
>>> dict_var.keys()
[1, 'c', 3, 'e', 5, 'f', 'b', 'd']
>>> dict_var.values()
[2, 'd', 'a', [5, 6, 7], 6, 8, 4, {'y': 21, 'x': 20}]
>>> dict_var
{1: 2, 'c': 'd', 3: 'a', 'e': [5, 6, 7], 5: 6, 'f': 8, 'b': 4, 'd': {'y': 21, 'x': 20}}
>>> del(dict_var[5])
>>> dict_var.pop('c')
'd'
>>> dict_var
{1: 2, 3: 'a', 'e': [5, 6, 7], 'f': 8, 'b': 4, 'd': {'y': 21, 'x': 20}}
>>> for key,val in dict_var.iteritems():
...     print key,val
1 2
3 a
e [5, 6, 7]
f 8
b 4
d {'y': 21, 'x': 20}
```

## Tuple

```
>>> tuple_var = (1, 2, 3, 4, 5, 'a string', 3, 2, 3, 'another string')
>>> len(tuple_var)
10
>>> tuple_var[5]
'a string'
>>> tuple_var[2:5]
(3, 4, 5)
>>> tuple_var.count(3)
3
>>> tuple_var.index(3)
2
```

## Object Identity
```
>>> d = 1
>>> e = 2.3
>>> f = 1
>>> id(d)
4298171656
>>> id(e)
4298179416
>>> id(f)
4298171656
>>> f = 2
>>> id(f)
4298171632
>>> f = e
>>> id(f)
4298179416
>>> e, d = d,e
>>> id(d)
4298179416
>>> id(e)
4298171656
>>> print d
2.3
>>> print e
1
```

## Object

Everything is an Object

```
>>> two = 2
>>> type(two)
<type 'int'>
>>> three = 3.4
>>> type(three)
<type 'float'>
>>>
```

```
>>> mystring= "a string with 'quotes'"
>>> mystring
"a string with 'quotes'"
>>> my string2 = 'a string with "quotes"'
  File "<stdin>", line 1
    my string2 = 'a string with "quotes"'
             ^
SyntaxError: invalid syntax
>>> my string2= 'a string with "quotes"'
  File "<stdin>", line 1
    my string2= 'a string with "quotes"'
             ^
SyntaxError: invalid syntax
>>> mystring2= 'a string with "quotes"'
>>> mystring
"a string with 'quotes'"
>>> mystring2
'a string with "quotes"'
>>> mystring3=""" a string with "quotes" and more 'quotes'"""
>>> mystring4='''a string with 'quotes' and more "quotse"'''
>>> mystring3
' a string with "quotes" and more \'quotes\''
>>> mystring4
'a string with \'quotes\' and more "quotse"'
>>> mystring5='a string with \"quotes\"'
>>> mystring5
'a string with "quotes"'
>>> mystring6='a string with \042quotes\042'
>>> mystring6
'a string with "quotes"'
>>> mystring7= 'a string with \047quotes\047'
>>> mystring7
"a string with 'quotes'"
>>>
```
