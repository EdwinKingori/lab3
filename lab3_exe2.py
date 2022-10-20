Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
str = "This sentence has 27 chars."
len(str)
27
str[-1]
'.'
str[len(str)]
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#3>", line 1, in <module>
IndexError: string index out of range
str[len(str)-1]
'.'
str[4]
' '
str[:4]
'This'
str[-6:]
'chars.'
str[-9:-7]
'27'
str[4:1]
''
str[-10:27]
' 27 chars.'
