Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 15
>>> "Gayathri" + 35
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    "Gayathri" + 35
TypeError: can only concatenate str (not "int") to str
>>> num1 = str(15)
>>> print("gayathri is ")+num1
gayathri is 
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("gayathri is ")+num1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
>>> print("Gayathri is " + num1)
Gayathri is 15
>>> num2= 45
>>> "My mother is "+`num2`
SyntaxError: invalid syntax
>>> print("my mother is " + `num2`)
SyntaxError: invalid syntax
>>> repr() // same as str
SyntaxError: invalid syntax
>>> name = "university"
>>> name[0]
'u'
>>> name[2]
'i'
>>> name[-1]
'y'
>>> name[-4]
's'
>>> name[2:5]
'ive'
>>> name[3:8]
'versi'
>>> name[:8]
'universi'
>>> name[3:]
'versity'
>>> name[:]
'university'
>>> len("university")
10
>>> len("Sabaragamuwa University")
23
>>> 
