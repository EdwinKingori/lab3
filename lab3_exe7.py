Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: /home/eddy/Documents/jenga school assignment/lab3/lab3_exe7.py ===
std = ["Ali", 1, 2.5, "Elif", 2, 3.0]
std[0]
'Ali'
std[-1]
3.0
type(std[2])
<class 'float'>
std[3]
'Elif'
std[3][2]
'i'
std[0 + 3]
'Elif'

std[0] + [3]
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#8>", line 1, in <module>
TypeError: can only concatenate str (not "list") to str
std [0:3]
['Ali', 1, 2.5]
std [::-1]
[3.0, 2, 'Elif', 2.5, 1, 'Ali']
std [-1] *2
6.0
